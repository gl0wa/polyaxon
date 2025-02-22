---
title: "Polyaxon Release notes"
sub_link: "release-notes"
meta_title: "Polyaxon release notes - Polyaxon Releases"
meta_description: "Polyaxon release notes, migrations, and deprecation notes."
visibility: public
status: published
tags:
    - reference
---

## 0.5.3

 * Upgrade python to 3.7.4.
 * Update default kaniko image tag to v0.9.0.
 * Add note about using pgbouncer for scaling connexions to DB. 
 * Add a conf caching mechanism to prevent hitting the db frequently when requesting config options.
 * Update default admin pages for builds, jobs, experiments, groups, tensorboards, notebooks.
 * Fix issue with registry access update form.
 * Add better handling for refresh auth tokens.
 * Make more defensive confirmation dialog by emphasising entities and actions.
 * Make project deletion harder by requiring the user to enter the project name.
 * Add more CLI checks for dependencies during deployment.
 * Make code path resolving consistent between local run and platform run.
 * Expose `maxConnAge` configuration option for both in-cluster and external postgresql connexion. 
 * Force user to re-login when token expires.
 * Make stream API internal.
 * Internal improvements.


## 0.5.2

 * Add asset version context processor.
 * Remove settings dropdown condition on admin interface.
 * Update health and status checks urls to follow best practices.
 * Fix jobs artifacts logging. 
 * Fix dockerfile path resolution for local runs.
 * Add a simple way to inject debug mode command (only CLI side).
 * Fix issue displaying artifacts for S3 stores.
 * Add docs for using Minio for logs/data/artifacts.

## 0.5.1

 * Add possibility to specify pod annotations for jobs/experiments/builds/notebooks/tensorboards.
   * By default polyaxon will inject necessary annotations, e.g. when using TPU.
   * Users can now define default annotations for each primitive cluster wide.
   * Polyaxonfile spec allows to override the annotations per run.
 * Add possibility to specify custom pod labels for jobs/experiments/builds/notebooks/tensorboards.
   * By default polyaxon uses recommended k8s labels for all managed resources.
   * Users can now define default custom labels for each primitive cluster wide.
   * Polyaxonfile spec allows to override the labels per run.
   * N.B. The custom labels cannot override Polyaxon's required labels.
 * strengthen statuses check and fall back to db check if keys are evicted.
 * Disable namespace monitoring by default.
 * Disable containers resources monitoring by default.
 * Expose several celery options by worker type.
 * Force rabbitmq confirmation when used as a broker by default.
 * Add gzip to list APIs by default
 * Remove parts requiring privileged mode when deploying Polyaxon.
 * Fix in-cluster redis node scheduling docs: uses master/slave.
 * Fix Helm chart validation when disabling docker-registry.
 * Fix issue detecting some local configs when running polyaxonfiles locally (use_https was not detected correctly).
 * Fix quick creation modes in UI.
 * Fix route for creating Tensorboard in UI.
 * Fix UI issues noticed in offline deployment: self-host all styling requirements.
 * Fix spelling in UI.
 * Fix polyaxonfile spec unable to handle quotes in commands.
 * Update lodash: vulnerability issue.
 

## 0.5.0

 * Add "Cluster Level Dynamic Configuration":
   * Move scheduling configuration to UI.
   * Move integrations to UI.
   * Move secrets and config maps catalogs to UI.
   * Move github/gitlab/bitbucket/azure authentication setup to UI.
   * Move private repos setup to UI.
   * More hardware accelerator setup to UI.
   * Add possibility to create an access catalog for registries and git repos.
   * Add possibility to create an access catalog for connections, data, logs, outputs. 
   * Move kaniko, default tensorboards config, default notebooks config to UI.  
 * Introduce security group with optional and configurable user UID and group GID for all Polyaxon services and scheduled runs.
 * Mount all volumes with the proper security context.
 * Add a warning when code is big.
 * Add possibility to specify a service account for jobs/experiments/builds/notebooks/tensorboards.
   * By default polyaxon uses a worker service account.
   * Users can now use a default service account for each primitive cluster wide.
   * Polyaxonfile spec allows to override the service account per run.
 * Add possibility to specify a default resources to use for jobs/experiments/builds/notebooks/tensorboards.
   * By default polyaxon schedules runs without resources.
   * Users can now set default resources to use for each primitive cluster wide.
   * Polyaxonfile spec allows to override the resources per run.
 * Add pod restarts.
   * By default polyaxon schedules runs without pod restarts.
   * Users can now set a default pod restarts to use for each primitive cluster wide.
   * Polyaxonfile spec allows to override the pod restarts per run.
 * Add minimum resources requirement for injected containers (init and sidecar).
   * This will fix the issue in clusters with pod security policy requiring that all pods must specify resources. 
 * Update redis chart and support using external/managed redis instance.
 * Update rabbitmq chart and support using external/managed rabbitmq instance.
 * Update docker-registry chart and support using external/managed docker registries.
 * Add possibility to turn-off rabbitmq completely and use Redis as broker instead.
 * Make .polyaxonignore honour .gitignore syntax.
 * Rename declarations section to params.
 * Add typing to Polyaxonfiles and schemas.
 * Extract polyaxon dockerizer logic to reuse in other environments.
 * Add possibility to run polyaxonfiles and update params without changing the yaml files: `polyaxon run -f polyaxonfile.yaml -P param1=value1 -P param2=value2`.
 * Add possibility to run polyaxonfiles locally. 
   * Allow to run experiments (non-distributed) locally either by invoking a python code with a conda/pip env or by generating a dockerfile, with out-of-the box tracking if POLYAXON_NO_OP is not set to true.
 * Deprecate docker registry authentication using user/password in favor of credential stores and credential helpers.
 * Add documentation for using ECR as Docker registry.
 * Mark kaniko stable: possibility to pull / push from any docker registry.
 * Mark jupyter lab stable.
 * Add sorting for outputs.
 * Update internal architecture to allow development and extending the platform with internal plugins.
 * Expose one single port for accessing all internal Polyaxon's APIs.
 * Update e2e tests with different deployments configurations.
 * Extend input schema to allow users to easily convert boolean params to flags in polyaxonfiles.
 * Add caching layer when checking statuses.
 * Add encryptor for managing sensitive data in-cluster with future possibility to use vault as a backend, currently the backend uses fernet encryption.
 * Add possibility to search entities by name or description using regex. 
 * Improve deployment using CLI, add new command: `polyaxon admin`.
 * Extend build kind with `lang_env` to easily export language environment.
 * Add initial work on early stopping policies for hyperparams tuning.
 * Add possibility to install auto-completion for polyaxon CLI.
 * Add possibility to invalidate individual builds and builds under a project.
 * Update API logic to save raw content to post-resolve contexts.
 * Add admin deploy/upgrade --dry_run commands for debugging purposes.
 * Add alpha version of Polyaxon on docker-compose.
 * Allow verify_ssl to be turned on via the CLI.
 * Improve init container stability by introducing retry on ConnectionError.
 * Improve docs for ingress's annotations.
 * Fix issues in log_artifact and log_artifacts.
 * Fix issue with default ssl path: SSL with node port service should not mount certs in /etc/ssl by default.
 * Fix issue when updating the internal API port.
 * Fix issue when using S3 as outputs storage.
 * Fix issue with the Helm chart not working correctly when RBAC is disabled (This is issue was noticed in Minikube with RBAC disabled).
 * Fix issue preventing to install Polyaxon with the latest helm version.
 * Fix issue with default build backend being ignored in some instances.
 * Fix issue breaking Jupyter lab theme in some recent versions.
 * Fix issue with scheduling S3 credentials for tensorboards.
 * Fix Experiment restart --copy creating additional folder.
 * Fix restart and resume experiments in groups not adding the new experiment to the same group.
 * Add resume button to UI. 
 * Add tensorflow tracking to contrib.
 * Improve keras tracking.
 * Add fastai tracking to contrib.
 * Remove several dependencies and replace with simple utils functions.
 * Add initial data/artifacts/logs stores and catalogs.
 * Add initial documentation for Polyflow: an actions/events pipeline engine for creating and automating machine learning workflows.
   * Allow to run ops in parallel while respecting concurrency in pipelines.
   * Allow to run pipelines following schedules: 2 interfaces intervals and crons.
   * Allow to run pipelines with complex ops dependencies as DAGs.
   * All to resolve ops' definitions, from inline templates, local templates, registries of actions/events.
   * Add initial work on supporting airflow out-of-the-box or possibility to easily port ops to Polyaxon to run container native operations.
 * Add templating for operationalizing and reusing Polyaxon's experiments and jobs.

## 0.4.4

This is a patch release on top of 0.4.3/0.4.2 containing no breaking changes., this version has no data or db migrations.

 * Fix issue with IntegrityError when creating large number of experiments.
 * Add error validation and redirection when creating experiments selection.
 * Add alpha version of configurable security context.
 * Update Polyaxon deploy to handle Minikube and MicroK8S.
 * Optimize and reduce size of official images.
 * Add dockgen package and initial work on local run mode.
 * Add docs for Polyaxon Client authentication options.
 * Update `log_artifact` and `log_artifacts` methods on the Experiment tracking API as an alternative to `experiment.outputs_stores.upload_file/dir`.
 * Fix Polyaxon Chart ingress issues and typos.
   
## 0.4.3

 * Re-enable possibility to create projects from dashboard.
 * Add possibility to create experiments, groups, jobs, and builds from dashboard
   * Different creation modes
   * Creation from current project or from top level by choosing a project
 * Add possibility to start notebooks for projects and tensorboards for projects, experiments, groups from the dashboard.
 * Add possibility to restart experiments from the dashboard.
 * Add tables for notebooks and tensorboards on the dashboard to easily see which tensorboards/notebooks are running or failing and their statuses.
 * Add possibility to stop notebooks and tensorboards from dashboard without going to the individual experiment/group/project. 
 * Add support for multiple secrets in ingress TLS.
 * Add support for Custom Cluster DNS resolvers.
 * Add support for any DNS backend, users deploying Polyaxon on Kubernetes created by Kubespray won't have to switch DNS from CoreDNS to KubeDNS anymore.
 * Add error handling for searches and metric views creation on dashboard.
 * Add proper error handling for dashboard forms and search UIs, show errors generated by frontend validation and server side validation.
 * Add loading indicators to differentiate between non-found entities and fetch in-progress.
 * Add notebooks and tensorboards search APIs.
 * Add several new fields to the search managers.
 * Move NFS-Provisioner from Polyaxon Chart to a separate repo, users can use the NFS-PROVISIONER maintained Helm chart 
   to deploy an NFS server to create MultiReadWrite volumes to use with Polyaxon. 
 * Add documentation on how to use the Provisioner for different aspects of the platform, i.e. data, logs, outputs, ...
 * Remove NGINX Ingress from Polyaxon chart, and create documentation on how to use setup an NGINX Ingress from the stable chart. 
   Users can also bring their own Ingress controller to use with the ingress resource provided in the chart. Polyaxon should work any ingress controller, 
   and docs will be updated to show how to use the major ones.
 * Add missing fields to the polyaxon deploy spec validation.
 * Add `polyaxon deploy` to deployment docs as it is now stable.
 * Add alpha version for parcoords visualization to experiment groups.
 * Add proper editor to show configs, dockerfiles, polyaxonfiles on the dashboard. 
 * Update searches and add some default searches (running, succeeded, and failed), more work to improve UI for creating searches and filters in the upcoming versions.
 * Fix issue with Docker client unable to authenticate to private DockerHub registries.
 * Add new docs section to show specific params needed to use private images on DockerHub.
 * Add SSL docs.
 * Add better handling for creating searches with similar names.
 * Update streams errors handling.
 * Fix some encoding issues and auth error handling in CLI.
 * Add docs/refs url shortcuts on the dashboard header. 
 * Update some packages that have some security and deprecation problems.
 * Remove `eventMonitors` from list of services to scale to prevent duplication of monitored cluster events, 
   and set it to a singleton on the chart to prevent other users from changing the value.
 * Several other internal fixes and improvements.
 * Fix issue requiring users to manually invalidate browser cache.
  

## 0.4.2

 * Add support of native Horovod experiments.
 * Add new fields for experiments: backend and framework.
   * Framework can be used for any experiment as a special field/tag.
   * When using distributed experiments, some frameworks are recognized and will trigger a particular behaviour.
   * Default backend is `native`, i.e. Polyaxon's native behaviour for spawning experiments, 
   additionally users can start distributed experiments on Kubeflow, by changing the backend field to `kubeflow`.
 * Add helm charts to easily deploy TFJob, PytorchJob, and MPIJob without requiring the user to install a full Kubeflow deployment.
 * Add spawners for distributed experiments on Kubeflow's operators: TFJob, PytorchJob, MPIJob.
 * Update distributed experiments logs handling
   * Streaming experiment's logs show all logs.
   * User can stream specific job's logs.
   * Experiment UI shows default job's logs + user can check specific logs of each job.
 * Update schema validation: now extra values or wrong values, even in nested sub-schemas, will raise a validation error.
 * Update icons version.
 * Polyaxon deploy is now in public beta and will be the recommended way to deploy/upgrade the platform.
 * Extend the build subsection behaviour to accepts an environment as well, now users can set the build resources and selectors for the build inside jobs and experiments.
 * Add possibility to download individual outputs files.
 * Fix a regression when downloading outputs from GCS.
 * Fix some issues with outputs tree view.
 * Fix some log formatting issues.
 * Fix readme style issues.
 * Fix some UI issues.
 * Fix some edge cases discovered when using Hyperband.
 * Fix an issue related to pending and initializing statuses not recognised correctly.
 * Several misc regressions fixed and internal enhancements.  
 

## 0.4.1

 * Add UI for experiment jobs (overview, logs, statuses).
 * Improve logging and logs archiving of distributed experiments.
 * Improve the header's tooltip behaviour.
 * Improve experiment UI by reducing number of tabs.
 * Improve a couple of queries resulting in large memory consumption.
 * Improve CI sync function to handle: 
   * Updating access tokens.
   * Force push mechanism.
   * Fetching of new branches
 * Fix build branch and commit handling, remove `ref` and add a more explicit fields: `commit` and `branch`. 
 * Fix regression in distributed experiments.
 * Fix an issue with experiment job's statuses creation dates.
 * Fix readme editor styles.
 * Fix charts UI adjustment.
 * Fix issue scheduling notebook on TPU.
 * Fix some issues related to corrupted UI state resulting in UI crashing. 
 * Update dependencies exposing security vulnerabilities.
 * Update several libraries to newer version.

## 0.4.0

 * Add configuration to set a default notebook image.
 * Add configuration to set the default notebook backend.
 * Add support for conda environments.
 * Add a first version Polyaxon CI.
 * Add a new status `stopping` for experiment groups to indicate that the scheduler is stopping experiments in the group and prevent others from starting.
 * Attempt solving an issue of high idle cpu usage caused by rabbitmq container.
 * Fix issues due to concurrency for handling and setting correct statuses for experiment jobs.
 * Fix regression in native build failed status.
 * Fix some issues related to concurrency.
 * Fix some issues when handling files are not found on buckets.
 * Fix updating unique names.
 * Fix several UI typos.

## 0.3.9

 * **important** This version supports only one outputs (either a store or a volume), to simplify deployment of the CE version and reduce confusion.
 * Refactor build process to support plugins and several backends
 * Make native builder lighter.
 * Add support for building containers with Kaniko as a backend in Beta.
 * Add possibility to use own dockerfile to build containers.
 * Add possibility to use contexts to to only mount sub-folders in a repo for specific tasks (e.g. mount /code/processing module for data extraction in job, and /code/training for training in experiments).
 * Add support for running Jupyter Labs in addition to Jupyter notebooks.
 * Allow in-cluster authentication when using notebooks (users can create experiment and track metrics/tags/params in notebooks created by Polyaxon seamlessly).
 * Improve jobs'/experiments' authentications.
 * Disable creation of polyaxonfile.yaml by default on `init` commands to allow users to put their polyaxonfiles wherever they want.
 * Improve usage of external repos (add support for using an access token or user/password).
 * Enable project to either use in-cluster code tracking or code on github/bitbucket/gitlab.
 * Update several internal components handling fetching, extracting and archiving external repos.
 * Improve notebooks build process: Current version only allows serverless notebooks (mounting in-cluster code will be re-enabled later).
 * Add several checks to Experiment Group Studies to prevent non-ending groups on errors.
 * Handle missing experiments in suggestion algorithms gracefully.
 * Enable logs on buckets (GCS/S3/Azure).
 * Re-enable tensorboards to continuously add experiments in project/groups as they outputs values.
 * Improve and separate deletion/archiving of projects/groups/experiments/jobs, and extend UI to support it.
 * Make default tensorboard image configurable. 
 * Make all components' logging level configurable with `logLevel`.
 * Extend `polyaxon run` to switch project context and run a config on any project, e.g. `polyaxon run -p projectA -f /polyaxonfiles/config1.yaml`.
 * Allow users to either upload code `polyaxon upload` or set external repo `polyaxon project git --url=https//... --private`, 
 so that code tracking can be either in-cluster or on external repos, next version will be introducing github/gitlab hooks to automate pushing to training.
 * Add `polyaon deploy` and `polyaxon teardown` to check a config deployment file, deploy a cluster, upgrade, or teardown in Beta.
 * Allow to customize TPU scheduling: default tensorflow version and resource key.
 * Improve installing cloud stores dependencies with polyaxon-client: `polyaxon-client[gcs]`, `polyaxon-client[s3]`, `polyaxon-client[azure]`.
 * Improve tracking of experiments logs running outside of Polyaxon.
 * Fix TPU scheduling.
 * Fix some issues preventing stopping unschedulable notebooks/tensorboards.
 * Fix detection of warning pod statuses.
 * Fix handling of k8s issues with wrong/bad annotation.
 * Fix issue with platform version returning inverted version values.
 * Fix issues interacting with cloud storages and handling of exceptions.
 * Fix some cli encoding issues in python2.x. 
 * Several internal enhancements.

## 0.3.8

 * Fix an issue with a cron job that handles the deletion of archived projects/jobs/experiments/builds.
 * Update ingress to allow users to create an ingress with an IP only without requiring a host.
 * Add `POLYAXON_NO_OP` option to the client/tracking api (polyaxon tracking operation will be ignored), 
 to allow users to perform a dry-run of their code when used outside of a Polyaxon context without crashing.
 * Add possibility to disable verify ssl for Polyaxon client and Polyaxon cli. 
 * Update default rabbitmq image version.
 * Several internal enhancements.
 
## 0.3.7

 * Add possibility to collect logs to a cloud storage bucket (S3/GCS/Azure storage).
 * Add keras callback for tracking metrics.
 * Add possibility to read client config from `.polyaxonclient` file as well as from env vars.
 * Add validation for values containing lists.
 * Add copy-to-clipboard to preserve configuration yaml structure when copying from browser.
 * Add confirmation dialogue before deleting/stopping entities on Dashborad.
 * Add better logs handling for in-cluster jobs and experiments running on other platforms.
 * Enable admin view by default with useful models only.
 * Enhance statuses watch.
 * Add gzip decorator for some endpoints.
 * Enhance stores and options management (internal improvements).
 * Add external registries for managing build images (Beta).
 * Add graceful Handling of wrongly detected gpu nodes.
 * Fix token auto-refresh.
 * Fix user deletion from admin UI.
 * Fis issue with declarations of type list not being handled correctly on dashboard.
 * Fix issue relates to `ls` on GCS.
 * Fix some issues related to detecting changes on Azure.
 * Fix error when the command `config --list` when the cli configuration is not initialized.  
 * Extend in-cluster examples.
 * Add examples for tracking experiments outside of Polyaxon.
 * Introduce Polyaxon deployment lifecycle management (Beta).

## 0.3.5

 * Update logging logic, logs are now collected lazily.
 * Use k8s logs timestamps to avoid lags between Polyaxon and k8s.
 * Expose pod name on experiments jobs, jobs, builds, tensorboards in UI & CLI.
 * Update sidecar logic, first step to implement a collector sidecar logic for artiacts/outputs.
 * Deletion of `projects`, `experiment groups`, `experiments`, `jobs`, is now asynchronous, and results in archiving the entity for a certain period.
 * Add archiving period, configurable with `cleaningIntervals.archived` default 7 days, to allow users to recover deleted entities, otherwise, archived entities older than this interval get cleaned.
 * Add support for TPU scheduling.
 * Fix study groups issue related to creating chunks of serializable numpy suggestions.
 * Schedule configmap and secret refs for builds created by experiments/jobs/notebooks.
 * [Security, XSS fixes] Update: bootstrap 3.4.0.
 * Update service account usage for workers to get less permissions.
 * Calculate run time based on running status instead of starting status, the reason is that an experiment can be sent to k8s scheduler, hence it can wait for some time for resources before it starts actually running.
 * Fix UI issue in the job overview tab.
 * Fix smoothing algorithm, was dropping the first metric resulting in wrong visualization, now the smoothing has similar behaviour to the Tensorboard's.
 * Disable ingress by default, and use LoadBalancer as default value for charts.
 * Add host list directly on ingress to use when tls is not enabled.
 * Remove deprecated `polyaxon-logs` service. 
 * Use ocular for monitoring statuses.
 * Use polystores for managing stores.
 
 
## 0.3.4
 
 * Add new statuses: "warning" and "unschedulable".
 * Extend specification to allow `run` to accept multiple commands in polyaxonfiles.
 * Add details information when an experiment is stopped by the system.
 * Allow to edit entities' names from the UI for group/experiment/job/build.
 * Display the name given by the user by default and fall back to the unique name generated by the platform.
 * Add UI meta info about the restarted/resumed/copied jobs/experiments and add ref to the original entity.
 * Add termination reason/status code to failed runs.
 * Fix issue with resumed experiments' outputs getting wrong artifacts.
 * Update statuses logging logic to not drop past events caused by concurrency.
 * Always insert statuses while respecting the state machine before the event was detected.
 * Remove default value for jobs cloning strategy (was added by mistake).
 * Fix issue fetching experiments' declarations in groups' metrics.
 * Fix an issue with stop job api.
 * Fix issue in sidecar monitor.
 * Fix bookmark tooltip style issue.
 * Update some UI styles.
 
## 0.3.3

 * Add download button for logs.
 * Add download button for outputs.
 * Make ephemeral tokens ttl a configurable param.
 * Optimize experiment group studies.
 * Extend specification to accept registries with port numbers in the build section.

## 0.3.2

 * Add `--init` option to `polyaxon create` to allow users to create and initialize a project at the same time.
 * Use `done` instead of `succeeded` for experiment groups status.
 * Upgrade image and python to 3.6.
 * Update the registration's validation.
 * Update smoothing algorithm: move from spline to moving average.
 * Add search algorithm to group schemas and to cli `polyaxon group get`.
 * Update heartbeat logic: start logic from running status instead of scheduled.
 * Update heartbeat logic: lower check frequency.
 * Move some abstractions from EE to CE.
 * Update error handling for download requests in client.
 * Update token with scopes and refresh mechanism.
 * Improve some apis.
 * Add mechanism to ensure CSRFToken refresh on page refresh.
 * Update kubernetes client.
 * Add dockerizer pull policy.
 * Fix nested outputs relative paths.
 * Fix tabs css behaviour outlining clicks.
 * Fix admin readonly mixin.
 * Fix issues with the ui client POST/DELETE/PATH requests.
 * Fix notebook UI actions.
 * Fix admin styles regression.

## 0.3.1

 * (Security) Add IPs/Hosts whitelist configuration.
 * (Security) Make admin view configurable and disable it by default.
 * Add api host/ip configuration to send emails/slack/notifications/integrations with clickable links.
 * Add more validation and edge cases handling for outputs apis.
 * Add loading indicator for dashboard.
 * Add migration to prepare for auth/permission plugins and extensions for the community version (Phase 1).
 * Remove experiment group schemas patch.
 * Minify styles.
 * Fix UI alignment and usability issues.
 * Fix an issue with groups' type not created for studies.

## 0.3.0

 * Add experiment selection groups: Users can now compare 2 (or more) experiments by adding them to a selection.
 * Add possibility to visualize metrics and to start a tensorboard for any selection of experiments.
 * Add outputs/artifacts tree view.
 * Add outputs/artifacts files (text/code/images) previewing.
 * Add tensorboard support for events on cloud storage (S3 and GCS).
 * Add refresh button to avoid reloading the whole page (first step to better UX, next step is real-time updates or polling). 
 * Extend tensorboard behaviour to show events from different backend storages (e.g. one experiment persisting events to S3 and another to GCS)
 * Add possibility to delete and stop multiple experiments at once.
 * Allow to configure heartbeat timeout.
 * Allow to support commands with `&&` without the need to create a script.
 * Connect gaps in charts, an issue happens when only a data point is created at a time.
 * Extend Groups Component to show the group type (study & selection).
 * Extend private registries to accept dictionaries as well as uri specs.
 * Open access for private repos to public beta. 
 * Add help text to indicate that names must be slugs (a better error handling for the dashboard is needed).
 * Add default node scheduling for tensorboards.
 * Upgrade security warning packages.
 * Enhance cloud storages management.
 * Fix an issue not showing all error logs of builds.
 * Fix an issue with cli existing if both `--past` and `--follow` are passed, and `past api` returns a 404.
 * Fix issues copy/restart experiment from a group.

## 0.2.9

 * Add Azure Storage to public beta.
 * Update SSO behaviour to create users inactive by default.
 * Add support for external public repos.
 * Add support for external private repos (beta).
 * Extend build specification with commit/branch(treeish) for both internal and external repos. 
 * Update and extract sidecar logic to independent service.
 * Add support for external experiment logging.
 * Update and enhance store management.
 * Trigger single build process for experiment groups.
 * Update behaviour of `latest` docker tag, default to not always pull, add configuration to set it up to True.
 * Update and fix several docs issues. 
 * Add port forwarding command docs
 * Add workload heartbeat tracking, jobs/experiments not reporting will be marked as Zombie runs.
 * Enhance internal events management, default is async now.
 * Add possibility to stop tensorboards/notebooks from dashboard.
 * Force experiment statuses to respect the transition matrix.
 * Update logging to track timestamps as well, cli logs commands have option to hide timestamps.
 * Extend health check logic with disk, memory, cache, ...
 * Extract common utils.
 * Remove external repos management.
 * Fix issue with client not reporting correctly last metrics (worker dies before finishing the request).
 * Fix issue with cli outdated param (async).
 * Fix issues related to image builds.
 * Fix some ui issues on safari.
 
## 0.2.8

 * Seamless integration of S3 and GCS is now in public beta, 
   users can load data from cloud storages as well as from persistent volumes and host nodes, 
   they can also manage their outputs and artifacts using these storages, 
   tensorflow's integration is seamless as well for model and checkpoints logging.
 * Fix some issues with Azure Storage (still in private beta). 
 * Add support for user's custom secrets and config maps, 
   users can extend Polyaxon runs and workloads with extra environment and secrets.
 * Improve experiments' metrics API by using a queue for frequent updates.
 * Increase throttling rate for metrics reporting.
 * Add possibility to edit charts.
 * Add more automation to chart titles based on metrics/params.
 * Add periodic worker to improve performance.
 * Add cleaning crons to remove old notifications and logs.
 * Add streams health status.
 * Add extra config and annotation to prevent IOError in long running requests.
 * Add draft for out-cluster logging.
 * Fix validation issue related to gitlab usernames containing dots.
 * Fix issue with re-enabling previously disabled nodes. 
 * Fix issues related to artifacts management and absolute paths on users machines.
 * Fix filtering typo for `id` dropdown.
 
## 0.2.7

 * Add experiment groups' metrics/visualizations.
 * Add experiments' metrics comparison.
 * Add readme and note taking on project/group/experiment/job's overviews.
 * (`Data Migration`) Update Experiment's last metric, it will include all values even if they were not reported at the current step. This is a new behaviour to allow user to aggregate and have an overview over 
 all values reported from previous steps/epochs' metrics.
 * Add tags editing from dashboard.
 * Add description editing from dashboard.
 * Add health status endpoint.
 * Add tracking API documentation.
 * Fix issue with hyperparameters tuning; experiment groups are stuck trying to sample new values when user requests larger number of experiments than the provided space (happens only when using discrete distributions).
 * Add is_continuous property to space values.
 * Fix issue with cli upload large files.
 * Fix issue with cli losing connection due to timeout.
 * Update annotation for mounting volumes with read-only option, the read-only is now applied to both the volume and the persistence claim.
 * Update error message for cli upload.
 * Fix `notebook -u` command, an old keyword was still being passed.
 * Update static files caching options.
 * Attempt to stabilize connection to broker(better solution is required).
 * Upgraded requirements.
 * Removed unused frontend dependencies.
 * Update throttling behavior for some endpoints. 

## 0.2.6

This is a patch release on top of 0.2.3 containing no breaking changes.

 * For issues in NodePort deployments: an issue arises with builds and with overall internal connection to api.
 * Improved response time for project/group/experiment detail apis (removed query annotations).
 * Fix some db warnings related to Jsonb default values.

## 0.2.5

This is a patch release on top of 0.2.3 containing no breaking changes.

 * Add `-l` option to `polyaxon run` to start log automatically after run command
 * Keep stream connection alive for logs (fix issue with ending sessions)
 
## 0.2.4

This is a patch release on top of 0.2.3 containing no breaking changes.

 * Update client auth: persist token after ephemeral login

## 0.2.3

 * Fix one major issue with events getting dropped, which led to experiments getting stuck in scheduled status.
 * Add out cluster tracking and instrumentation, users can now track experiment outside of Polyaxon and compare the experiments in Polyaxon.
 * Add possibility to create experiment and experiment groups without polyaxon specification, to allow users to run custom hyperparams tuning.
 * Add ttl and debug mode for runs.
 * Add customizable charts.
 * Add chart views saving functionality.
 * Add metrics views.
 * Extend query spec api to save metrics/params columns.
 * Add group metrics visualization and analysis [Beta].
 * Improve stability of experiment groups (some issues are still under investigation).
 * filter disabled nodes out from cluster api end points.
 * Add possibility to use GCE/S3/Azure as an outputs and artifact storage [Beta].
 * Update handling of internal tokens to increase job/experiment security and scoping.
 * Add traceback to the failure event status to get more context.
 * Add code reference endpoint for jobs and experiments.
 * Add data references tracking and extend experiment details api.
 * Add run environment tracking and extend experiment details api.
 * Add handling for evicted pods.
 * Init should not reinitialize ignore files and other cli config files.
 * Introduce ephemeral auth for experiment and jobs.
 * Update code reference to include branch, url, is_dirty.
 * Add possibility to merge-update tags and params/declarations.
 * Extract env var handling and typing.
 * Fix group stats (counts of experiments in different stages)
 * Fix a UI issue with flexbox in last chrome
 
## 0.2.2

This is a patch release on top of 0.2.0 containing only bug fixes and no breaking changes or features.

 * Fix issue with web hooks not serializing events correctly

## 0.2.1

This is a patch release on top of 0.2.0 containing only bug fixes and no breaking changes or features.

 * Fix issue with serializing experiment jobs' tolerations

## 0.2.0

 * Enhance filtering and sorting: better UI and dropdown with filter/sort options
 * Add saved queries
 * Experiments table dashboard can include optional columns: metrics and declarations/params. This will allow to compare experiments in one table.
 * Update log stream to show phase changes instead of disconnecting the session (now you can run and log without providing any id or checking the build)
 * Add REST API docs
 * Include bookmark indicator in dashboard lists
 * Refetch on tab changes to get latest updates
 * Remove some javascript dependencies and reduce bundle size
 * Add cli install to `install.polyaxon.com`
 * Add exception handling for actions, errors were preventing experiments/jobs from running
 * Lint helm chart
 * Add helm chart CI
 * Fix an issue with csrf token collection
 * Fix issue in reducer that made the state inconsistent
 * Fix an issue with dashboard pagination
 * Fix issue with bookmark page not loading experiments, and only loading when navigating tabs
 * Fix a bug that made loading experiments slow

## 0.1.9

 * Add config deployment app to help guide users through the configuration options when deploying Polyaxon
 * Add possibility to delete/stop jobs/experiments from dashboards
 * Update charts to support rolling updates
 * Optimize and fix some issues in some API endpoints
 * Optimize and reduce number of generated queries (More queries to optimize)
 * Update SDK to expose only one client
 * Add a delay before creating the experiment group's experiment to avoid not finding running status
 * Extend config manager to validate different generic specs and raise errors on bad config deployments
 * Abstract serialization of bookmarks to be used for lists
 * Fix an issue with the metrics api's pagination
 * Enhanced the filters ui
 * Consolidate installed libraries

## 0.1.8

  * Enable users to pull image from private registries
  * Add first version of an abstraction to seamlessly use cloud storage or persistent volumes for data, outputs, and logs
  * Annotate jobs with node used for the scheduling
  * Remove some optional env vars and move them to default values
  * Use configMap and secret envFrom to populate environment
  * Reduce number of partials
  * Update default page size to 20
  * Update usage of secrets and configs
  * Update clean commands
  * Fix an issue with check command
  * Fix a bug related to checking running experiment groups
  * Add missing tests for azure id creation
  * Enhance build and test process
  * Upgrade kubernetes client to 6.0.0
  * Upgrade web socket and request libs
  * Upgrade api and workers requirements
  * Update test requirements
  * Move label and pod/job states schemas to core

## 0.1.7

  * Add initial draft of actions
  * Add base integrations mechanism
  * Add notification via emai, slack, pagerduty, mattermost, discord, hipchat, webhooks ...
  * Enlarge docker's shm memory
  * Fix Microsoft authentication
  * Fix issue with cleaning pre-delete hooks
  * Remove deprecated polyaxon-lib
  * Separate email and admin user in helm chart
  * Fix api service with NodePort
  * Fix issue related to delete project command outside of initialized polyaxon workspace in CLI
  * Redirect directly to dashboard from CLI

## 0.1.6

  * Add possibility to deploy Polyaxon with tls.
  * Expose default toleration/affinity for builds, jobs, experiments.
  * Add affinity and toleration to spec environment.
  * Update spec to use node_selector instead of node_selectors.
  * Refactor worker/ps/default_worker/default_ps in environment section.
  * Update CLI init command to always create a new config for the project.
  * Add shortcuts -f for follow and -p for past for the logs commands.
  * Creating job/build/experiment/group with cli will cache the instance automatically for the following commands.
  * Fix some command suggestions.
  * Upgrade pyyaml, there was a security issue.
  * Improve docker build process.
  * Fix pytorch distributed example.
  * Update chart cleaning hook delete strategy.
  * Fix an issue with detecting the correct k8s minor version.
  * Fix issue with docker build process: image name should be lower case.
  * Fix Run meta info for builds, jobs, and groups on dashboard.
  * Add draft for stats and actions.

## 0.1.5

  * Build images: You can now pip install any file in your code folder without the need to call the file polyaxon_requirements.txt. Same thing if you need to build an image and have a shell script you just need to chmod +x the file and add it to the build setps.
  * Add bookmarking: You can bookmark your projects/groups/experiments/jobs/builds with Dashboard/API/CLI/Client. If your team is running too many hyper params tuning in many projects, finding the important experiments/jobs/builds can be exhausting since it requires searching each time. Bookmarks allow you to easily save important runs and have access to them in an easy way.
  * Add activity logs: shows recent create/update/delete activities in your team cluster or projects.
  * Add history/recently viewed: This is also something that some teams showed a lot of interests in having, using the platform for a couple of weeks/months and creating thousands of experiments per day, makes it very hard to access the right information.
  * Add support for external PostgreSQL: it's possible to link an external PostgreSQL database instead of the in-cluster one.
  * SSO: Add support for Microsoft Azure authentication. in addition to github, gitlab, bittbucket, and LDAP, now you can allow your team to signup/login to Polyaxon with Microsoft Azure authentication
  * Tooltips: for dates (creation date, update date, starting date, termination date) the dashboard shows a humanized version (e.g. X hours/days ago) this was not super helpful, and many users asked to have the possibility to see the exact values. On your dashboard you can see the dates values by hovering on any date and it will show datetime in the "YYYY-MM-DD HH: mm:ss" format.
  * Add docs for replication: the docs now has a section outlining different strategies for replicating Polyaxon.
  * Add docs for postgres HA strategies.
  * Add docs for Microsoft Azure authentication.

## 0.1.4

  * Fix some issues with node discovery
  * Optimize access to k8s api
  * Update image build process
  * Optimize resources monitoring on k8s
  * Add bookmarks for project, groups, experiments, jobs, builds
  * Fix some UI issues
  * Update docs
  * Other changes from 🇷🇺

## 0.1.3

  * Add support for outputs reference from other jobs and experiments by id and name
  * Update metrics tab with empty metrics
  * Add some error handling for spec validation
  * Fix the instruction pages

## 0.1.2

  * Update instructions tabs
  * Expose commit on the query spec
  * Add query spec docs
  * Add statuses tab
  * Add metrics tab
  * Add jobs cleaning
  * Update logic for allowing commits after delete notebooks
  * Update outputs logics for tensorboards

## 0.1.1

  * Update dockerizer process: moved from a worker based process that handles image builds to pod being scheduled to build the image if does not exists
  * Possibility to force rebuilding an image
  * Separate run into 2 sections: run and build
  * Add build specification
  * Add tensorboard and notebook specifications
  * Add generic job specification
  * Optimize services images and reduce their sizes
  * Upgrade docker client
  * upgrade kubernetes client
  * Add and test replication for api, workers, and monitors
  * Add tagging for projects, experiments, experiments groups, and jobs
  * Add possibility to name runs (experiments, groups, jobs, builds)
  * Add filtering, you can now filter based on our query spec: started_at:2015-01-01..2018-01-20, tags:foo|bar, metrics__loss:<=0.1
  * Add sorting, you can now sort by different attributes: -created_at, updated_at...
  * Remove upper limit on hptuning, this will allow hptuning algorithm worker to consume more cpu and converge faster.
  * Add download code: you can see now the commit made internally each time you upload the code
  * Add outputs download for experiments and jobs
  * Update tensorboards to support not only projects but also experiments and experiment group
  * Update and enhance ui
  * Add possibility to mount multiple data and outputs volumes
  * Extend the specification to allow to choose an output and data volumes to mount for an experiment or a job
  * Fix several usability and stability issues
  * Extend experiments api to allow to pull metrics and declarations

## 0.1.0

  * Add LDAP auth backend
  * Add identity abstraction for oauth and integrations
  * Add Github oauth
  * Add Bitbucket oauth
  * Add Gitlab oauth
  * Update landing page and dashboard design
  * Update signup/login pages
  * Update behaviour of experiment groups finished status
  * Expose more params for Bayesian optimization (algorithm was not converging sometime because of the default n_iter and n_warmup value)
  * Add more experiment group meta data: run dates and total time, iterations, status, and algorithm search
  * Fix issues with parsing numpy types in specification files

## 0.0.9

  * Optimize build process and handle concurrent build of the same repo: this will fix issues related to experiment getting stack in the build process and sometimes preventing the iterative hyperparameters algorithms from continuing the search.
  * Add advanced nodes scheduling for experiments and jobs: Previously users could set a default node selectors for core and experiments. Now they have the ability to override these selectors per experiment, experiment job for distributed runs, notebook, and tensorboard.
  * Fix upload command on Windows platform
  * Add more edge cases handling for resumed experiments
    * deleting original should delete resumed experiments
    * resuming a resumed experiment should resume the original experiment
  * Fix issue with stopping experiment groups
  * Add NFS provisioner, this is practical for testing the platform without the need to create a real NFS server.
  * Add event management and backbone for creating notifications and integrations
  * Add tracker
  * Add activity log
  * Update docs requirement

## 0.0.8

  * Add restart/resume/copy experiments
  * Fix issue with cyclic redirection when the user's session is expired.
  * Add platform logging
  * Update Bayesian optimization
  * Fix prospector for tests
  * Remove requirement for project name in specifications
  * Add google GKE tutorial

## 0.0.7

  * This new version has breaking changes:
  * Update specification
    * Add kind section to indicate the type of operation to run on Polyaxon.
    * Rename sequential search to grid search
    * Update early stopping schema to use optimization instead of higher: maximize | minimize
    * Move matrix to settings
    * Add config for search algorithms to settings
    * Remove run_type and export strategies form settings
    * All early_stop to stop both individual experiment from running or an experiment group or both.
    * Rename steps to build_steps in run section
    * Rename concurrent_experiment to concurrency
    * Add new method for sampling values
    * Possibilty to provide a seed
    * Rename Sequential search to grid search
  * Add new hyperparameters search algorithms:
    * Add hyperband
    * Add bayesian optimization [alpha]
  * Add continuous methods for sampling matrix params:
    * pvalues
    * uniform
    * quniform
    * loguniform
    * qloguniform
    * normal
    * qnormal
    * lognormal
    * qlognormal
  * Add first version of pipelines.
  * Show logs after experiment is finished [api, ui, client, cli].
  * Optimize plugin jobs [tensorboards and notebooks].
  * Separate dahsboard and runner.
  * Fixed bug issues.

## 0.0.6

 * Enhance single experiment spawner
 * Add MXNet spawner and support for distributed MXNet experiments
 * Add Pytorch spawner and support for distributed Pytorch experiments
 * Add Horovod spawner and support for distributed Horovod experiments [WIP]
 * Optimize Tensorflow spawner and distributed Tensorflow experiments
 * Optimize schedulers' logic
 * Optimize docker build process

## 0.0.5

 * Add early stopping and number of experiments
 * Use statuses for jupyter notebooks and tensorboards
 * Fix issue with starting multiple tensorboards
 * Rename deleted status to stopped
 * Add admin dashboard

## 0.0.4

 * Add Jupyter notebooks
 * Update Tensorboard deployments
 * Apply project permission to project plugin jobs, i.e. tensorboard and notebooks will only be accessible to users with enough project permissions
 * Update dashboard and ui
 * Fix some issues with kubernetes resources tracking

## 0.0.3

## 0.0.2

