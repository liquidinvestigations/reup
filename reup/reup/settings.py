import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = os.environ.get('SECRET_KEY')

_hostname = os.environ.get('REUP_HOSTNAME')
if _hostname:
    REUP_BASE_URL = 'https://' + _hostname
    ALLOWED_HOSTS = [_hostname]


def bool_env(value):
    return (value or '').lower() in ['on', 'true']


DEBUG = bool_env(os.environ.get('DEBUG'))


INSTALLED_APPS = [
    'revive.apps.ReviveConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'reup.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'reup.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'reup',
    },
}

# heroku-style db config
_db = os.environ.get('REUP_DB')
if _db:
    dbm = re.match(
        r'postgresql://(?P<user>[^:]+):(?P<password>[^@]+)'
        r'@(?P<host>[^:]+):(?P<port>\d+)/(?P<name>.+)',
        _db,
    )
    if not dbm:
        raise RuntimeError("Can't parse REUP_DB value %r" % _db)
    DATABASES['default']['HOST'] = dbm.group('host')
    DATABASES['default']['PORT'] = dbm.group('port')
    DATABASES['default']['NAME'] = dbm.group('name')
    DATABASES['default']['USER'] = dbm.group('user')
    DATABASES['default']['PASSWORD'] = dbm.group('password')


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
