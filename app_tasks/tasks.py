# Celery
# from celery.decorators import task
from app_tasks.celery import app

import time

@app.task(name='test_task', max_retries=3)
def test_task():
    for i in range(5):
        time.sleep(1)
        print("sleeping", str(i+1))

