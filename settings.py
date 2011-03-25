import os
PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

LOCAL = False
DEBUG = True


TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('Gabriel Novaes', 'semproblema@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',# Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'easy_news',                 # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'root',                  # Not used with sqlite3.
        'HOST': 'localhost',                 # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '8889',                      # Set to empty string for default. Not used with sqlite3.
    }
}

EMAIL_HOST = ''	#ex: smtp.gmail.com
EMAIL_HOST_USER = 'seuemail@gmail.com' #ex
EMAIL_HOST_PASSWORD = '' 
EMAIL_SUBJECT_PREFIX = '[Easy News]'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

TIME_ZONE = 'America/Campo_Grande'

LANGUAGE_CODE = 'pt-br'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

MEDIA_ROOT = os.path.join(PROJECT_ROOT_PATH, 'media')

MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/admin_media/'

SECRET_KEY = 't#d&vqv4v4-ns%xm_j(45n3g6r1=nvp0mqv&fvxofg6-*%56=c'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
	'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
	os.path.join(PROJECT_ROOT_PATH,'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
	'django.contrib.admin',
	'django.contrib.syndication',
	'django.contrib.flatpages',	
	
	'galeria',	
	'noticias',
	'enquetes',

)

# tenta incluir local_setting.py se nao vai com esse mesmo
try:
    from local_settings import *
except ImportError:
    pass
