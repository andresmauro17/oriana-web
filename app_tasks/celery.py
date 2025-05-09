"""Celery app config."""

import os
from celery import Celery
from django.apps import apps, AppConfig
from django.conf import settings

from dotenv import load_dotenv

# Load dot env
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PATH_DOT_ENV = f'{BASE_DIR}/.env'
load_dotenv(dotenv_path=PATH_DOT_ENV)

if not settings.configured:
    
    # set the default Django settings module for the 'celery' program.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', os.environ.get('APP_ENV_SETTINGS'))
    


app = Celery('apps')
# Using a string here means the worker will not have to
# pickle the object when using Windows.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')


class CeleryAppConfig(AppConfig):
    name = 'app_tasks'
    verbose_name = 'Celery Config'

    def ready(self):
        installed_apps = [app_config.name for app_config in apps.get_app_configs()]
        app.autodiscover_tasks(lambda: installed_apps, force=True)


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')  # pragma: no cover

