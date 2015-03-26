from .base import *
import dj_database_url
import os

try:
	from .base import *
except ImportError:
	pass

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {'default': dj_database_url.config()}

#Env Variables
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PD_Hub.settings.production")
os.environ.setdefault("NPM_CONFIG_PRODUCTION", "true")


