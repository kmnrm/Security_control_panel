import os
from dotenv import load_dotenv
import dj_database_url
from distutils.util import strtobool

load_dotenv(override=True)

DATABASES = {}
DB_DEFAULT = os.getenv('DATABASE_URL')

DATABASES['default'] = dj_database_url.config(default=DB_DEFAULT, conn_max_age=None)

SECRET_KEY = os.getenv('SECRET_KEY')

INSTALLED_APPS = ['datacenter']

DEBUG = os.getenv('DEBUG')
DEBUG = bool(strtobool(DEBUG.lower()))

ROOT_URLCONF = "project.urls"

ALLOWED_HOSTS = ['*']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
