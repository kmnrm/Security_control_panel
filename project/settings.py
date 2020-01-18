import os
from dotenv import load_dotenv

load_dotenv(override=True)

DATABASES = {}
DB_SETTINGS = [
    'ENGINE',
    'HOST',
    'PORT',
    'NAME',
    'USER',
    'PASSWORD'
]

DATABASES['default'] = {
    setting: os.getenv(setting) for setting in DB_SETTINGS
    }

SECRET_KEY = os.getenv('SECRET_KEY')


INSTALLED_APPS = ['datacenter']


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
