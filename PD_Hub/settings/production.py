from .base import *
import dj_database_url
import os


DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {'default': dj_database_url.config(default=os.environ.get('HEROKU_PSTGRS_URL'))}

#Env Variables
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PD_Hub.settings.production")
os.environ.setdefault("NPM_CONFIG_PRODUCTION", "true")

try:
	from .local import *
except ImportError:
	pass
