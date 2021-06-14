import os

from celery import Celery

from dotenv import load_dotenv

import time

# Load dot env
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH_DOT_ENV = f'{BASE_DIR}/.env'
load_dotenv(dotenv_path=PATH_DOT_ENV)

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', os.getenv('APP_ENV_SETTINGS'))

## Get the base REDIS URL, default to redis' default
BASE_REDIS_URL = os.getenv('REDIS_URL')
print(BASE_REDIS_URL)

app = Celery('config')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.broker_url = BASE_REDIS_URL

# this allows you to schedule items in the Django admin.
app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
    # do something
    for i in range(30):
        time.sleep(1)
        print("sleeping", str(i+1))


# https://www.codingforentrepreneurs.com/blog/celery-redis-django