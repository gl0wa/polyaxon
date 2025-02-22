import json
import random

from hestia.auth import AuthenticationTypes
from hestia.crypto import get_hmac
from hestia.internal_services import InternalServices
from kubernetes.config import ConfigException

import conf

from constants.k8s_jobs import NOTEBOOK_JOB_NAME
from libs.paths.projects import get_project_repos_path
from libs.unique_urls import get_notebook_health_url
from options.registry.k8s import K8S_INGRESS_ANNOTATIONS
from options.registry.notebooks import NOTEBOOKS_BACKEND, NOTEBOOKS_PORT_RANGE
from options.registry.persistence import REPOS_CLAIM_NAME, REPOS_HOST_PATH, REPOS_MOUNT_PATH
from options.registry.spawner import APP_LABELS_NOTEBOOK, ROLE_LABELS_DASHBOARD
from polyaxon_k8s.exceptions import PolyaxonK8SError
from polypod.project_job import ProjectJobSpawner
from polypod.templates import constants, ingresses, services
from polypod.templates.env_vars import get_internal_env_vars
from polypod.templates.labels import get_labels
from polypod.templates.notebooks import manager
from polypod.templates.restart_policy import get_deployment_restart_policy
from polypod.templates.volumes import (
    get_auth_context_volumes,
    get_pod_refs_outputs_volumes,
    get_pod_volumes,
    get_shm_volumes,
    get_volume,
    get_volume_mount
)


class NotebookSpawner(ProjectJobSpawner):
    def __init__(self,
                 project_name,
                 project_uuid,
                 job_name,
                 job_uuid,
                 k8s_config=None,
                 namespace='default',
                 version=None,
                 in_cluster=False,
                 job_container_name=None,
                 job_docker_image=None,
                 sidecar_container_name=None,
                 sidecar_docker_image=None,
                 role_label=None,
                 type_label=None,
                 use_sidecar=False,
                 sidecar_config=None,
                 log_level=None):
        self.resource_manager = manager.ResourceManager(
            namespace=namespace,
            version=version,
            name=NOTEBOOK_JOB_NAME,
            project_name=project_name,
            project_uuid=project_uuid,
            job_name=job_name,
            job_uuid=job_uuid,
            job_docker_image=job_docker_image,
            job_container_name=job_container_name,
            sidecar_container_name=sidecar_container_name,
            sidecar_docker_image=sidecar_docker_image,
            role_label=role_label,
            type_label=type_label,
            use_sidecar=use_sidecar,
            sidecar_config=sidecar_config,
            health_check_url=get_notebook_health_url(job_name),
            log_level=log_level)
        super().__init__(project_name=project_name,
                         project_uuid=project_uuid,
                         job_name=job_name,
                         job_uuid=job_uuid,
                         k8s_config=k8s_config,
                         namespace=namespace,
                         in_cluster=in_cluster)
        self.port = self._get_plugin_port(NOTEBOOK_JOB_NAME)

    def get_notebook_url(self):
        return self._get_service_url(NOTEBOOK_JOB_NAME)

    def get_notebook_token(self):
        return get_hmac(conf.get(APP_LABELS_NOTEBOOK), self.project_uuid)

    @staticmethod
    def get_notebook_code_volume():
        volume = get_volume(volume=constants.REPOS_VOLUME,
                            claim_name=conf.get(REPOS_CLAIM_NAME),
                            host_path=conf.get(REPOS_HOST_PATH))

        volume_mount = get_volume_mount(volume=constants.REPOS_VOLUME,
                                        volume_mount=conf.get(REPOS_MOUNT_PATH))
        return volume, volume_mount

    def request_notebook_port(self):
        if not self._use_ingress():
            return self.port

        labels = 'app={},role={}'.format(conf.get(APP_LABELS_NOTEBOOK),
                                         conf.get(ROLE_LABELS_DASHBOARD))
        ports = [service.spec.ports[0].port for service in self.list_services(labels)]
        port_range = conf.get(NOTEBOOKS_PORT_RANGE)
        port = random.randint(*port_range)
        while port in ports:
            port = random.randint(*port_range)
        return port

    def get_notebook_args(self,
                          deployment_name,
                          mount_code_in_notebooks=False,
                          backend=None):
        backend = backend or conf.get(NOTEBOOKS_BACKEND)
        notebook_token = self.get_notebook_token()
        notebook_url = self._get_proxy_url(
            namespace=self.namespace,
            job_name=NOTEBOOK_JOB_NAME,
            deployment_name=deployment_name)

        if mount_code_in_notebooks:
            notebook_dir = get_project_repos_path(self.project_name)
            notebook_dir = '{}/{}'.format(notebook_dir, notebook_dir.split('/')[-1])
        else:
            notebook_dir = '.'

        return [
            "jupyter {backend} "
            "--no-browser "
            "--port={port} "
            "--ip=0.0.0.0 "
            "--allow-root "
            "--NotebookApp.token={token} "
            "--NotebookApp.trust_xheaders=True "
            "--NotebookApp.base_url={base_url} "
            "--NotebookApp.notebook_dir={notebook_dir} ".format(
                backend=backend,
                port=self.port,
                token=notebook_token,
                base_url=notebook_url,
                notebook_dir=notebook_dir)]

    def get_init_env_vars(self):
        env_vars = get_internal_env_vars(service_internal_header=InternalServices.INITIALIZER,
                                         namespace=self.namespace,
                                         authentication_type=AuthenticationTypes.INTERNAL_TOKEN,
                                         include_internal_token=True)
        return env_vars

    def start_notebook(self,
                       persistence_outputs=None,
                       persistence_data=None,
                       outputs_refs_jobs=None,
                       outputs_refs_experiments=None,
                       resources=None,
                       labels=None,
                       annotations=None,
                       secret_refs=None,
                       config_map_refs=None,
                       node_selector=None,
                       affinity=None,
                       tolerations=None,
                       backend=None,
                       max_restarts=None,
                       reconcile_url=None,
                       mount_code_in_notebooks=False):
        ports = [self.request_notebook_port()]
        target_ports = [self.port]
        volumes, volume_mounts = get_pod_volumes(persistence_outputs=persistence_outputs,
                                                 persistence_data=persistence_data)
        refs_volumes, refs_volume_mounts = get_pod_refs_outputs_volumes(
            outputs_refs=outputs_refs_jobs,
            persistence_outputs=persistence_outputs)
        volumes += refs_volumes
        volume_mounts += refs_volume_mounts
        refs_volumes, refs_volume_mounts = get_pod_refs_outputs_volumes(
            outputs_refs=outputs_refs_experiments,
            persistence_outputs=persistence_outputs)
        volumes += refs_volumes
        volume_mounts += refs_volume_mounts
        shm_volumes, shm_volume_mounts = get_shm_volumes()
        volumes += shm_volumes
        volume_mounts += shm_volume_mounts

        context_volumes, context_mounts = get_auth_context_volumes()
        volumes += context_volumes
        volume_mounts += context_mounts

        if mount_code_in_notebooks:
            code_volume, code_volume_mount = self.get_notebook_code_volume()
            volumes.append(code_volume)
            volume_mounts.append(code_volume_mount)

        resource_name = self.resource_manager.get_resource_name()
        args = self.get_notebook_args(deployment_name=resource_name,
                                      mount_code_in_notebooks=mount_code_in_notebooks,
                                      backend=backend)
        command = ["/bin/sh", "-c"]
        labels = get_labels(default_labels=self.resource_manager.labels, labels=labels)
        deployment = self.resource_manager.get_deployment(
            resource_name=resource_name,
            volume_mounts=volume_mounts,
            volumes=volumes,
            labels=labels,
            env_vars=None,
            command=command,
            args=args,
            init_env_vars=self.get_init_env_vars(),
            persistence_outputs=persistence_outputs,
            persistence_data=persistence_data,
            outputs_refs_jobs=outputs_refs_jobs,
            outputs_refs_experiments=outputs_refs_experiments,
            secret_refs=secret_refs,
            config_map_refs=config_map_refs,
            resources=resources,
            annotations=annotations,
            ephemeral_token=None,
            node_selector=node_selector,
            affinity=affinity,
            tolerations=tolerations,
            ports=target_ports,
            init_context_mounts=context_mounts,
            reconcile_url=reconcile_url,
            max_restarts=max_restarts,
            restart_policy=get_deployment_restart_policy(max_restarts))
        dep_resp, _ = self.create_or_update_deployment(name=resource_name,
                                                       body=deployment,
                                                       reraise=True)
        service = services.get_service(
            namespace=self.namespace,
            name=resource_name,
            labels=self.resource_manager.get_labels(),
            ports=ports,
            target_ports=target_ports,
            service_type=self._get_service_type())
        service_resp, _ = self.create_or_update_service(name=resource_name,
                                                        body=service,
                                                        reraise=True)
        results = {'deployment': dep_resp.to_dict(), 'service': service_resp.to_dict()}

        if self._use_ingress():
            annotations = json.loads(conf.get(K8S_INGRESS_ANNOTATIONS))
            paths = [{
                'path': '/notebooks/{}'.format(self.project_name.replace('.', '/')),
                'backend': {
                    'serviceName': resource_name,
                    'servicePort': ports[0]
                }
            }]
            ingress = ingresses.get_ingress(namespace=self.namespace,
                                            name=resource_name,
                                            labels=self.resource_manager.get_labels(),
                                            annotations=annotations,
                                            paths=paths)
            self.create_or_update_ingress(name=resource_name, body=ingress, reraise=True)
        return results

    def stop_notebook(self):
        resource_name = self.resource_manager.get_resource_name()
        try:
            self.delete_deployment(name=resource_name, reraise=True)
            self.delete_service(name=resource_name)
            if self._use_ingress():
                self.delete_ingress(name=resource_name)
            return True
        except (PolyaxonK8SError, ConfigException):
            return False
