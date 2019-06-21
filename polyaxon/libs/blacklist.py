from django.core.exceptions import ValidationError

NAME_BLACKLIST = {
    'user',
    'admin',
    'experiment',
    'experiment_group',
    'experimentgroup',
    'project',
    'api',
    'polyaxon',
    'dashboard',
    'index',
    'log',
    'metric',
    'portfolio',
    'public',
    'revision',
    'version',
    'support',
    'tryout',
    'output',
    'artifact',
    'data',
    'dataset',
    'secret',
    'config_map',
    'pod',
    'deployment',
    'model',
    'management',
    'dependency',
    'dependencie',
    'repo',
    'cluster',
    'event',
    'manage',
    'login',
    'account',
    'register',
    'accept',
    'organization',
    'team',
    'help',
    'doc',
    'logout',
    '404',
    '500',
    'static',
    '_static',
    'status',
    'statuses',
    '_status',
    'out',
    'debug',
    'remote',
    'cli',
    'blog',
    'welcome',
    'feature',
    'customer',
    'integration',
    'signup',
    'pricing',
    'subscribe',
    'enterprise',
    'about',
    'job',
    'thank',
    'guide',
    'privacy',
    'security',
    'term',
    'from',
    'sponsorship',
    'for',
    'at',
    'platform',
    'branding',
    'vs',
    'answers',
    '_admin',
    'support',
    'contact',
    'ext',
    'extension',
    'plugin',
    'notebook'
    'bookmark',
    'bookmarking',
    'tensorboard',
    'pipeline',
    'dag',
    'operation',
    'action',
    'task',
    'monitor',
    'setting',
    'legal',
    'avatar',
    'self',
    'this'
}
NAME_BLACKLIST |= {'{}s'.format(b) for b in NAME_BLACKLIST}


def validate_blacklist_name(name: str) -> None:
    """Validates slug name against a blacklist"""
    if name is None:
        raise ValidationError('A short name must be supplied.')

    if name.lower() in NAME_BLACKLIST:
        raise ValidationError('The name is a reserved word or already taken.')
