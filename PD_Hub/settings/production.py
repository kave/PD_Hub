from .base import *
import dj_database_url
import os


DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES['default'] = dj_database_url.config()
# Enable Connection Pooling
DATABASES['default']['ENGINE'] = 'django_postgrespool'

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

#Env Variables
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PD_Hub.settings.production")
os.environ.setdefault("NPM_CONFIG_PRODUCTION", "true")

try:
	from .local import *
except ImportError:
	pass
