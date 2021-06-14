from django.utils import timezone
# from apps.devices.models import Device
from celery import shared_task
import os

import time


@shared_task
def pull_attributes(device_id=None, **kwargs):
    """
    Pulls attribute data from the device vendor's API,
    stores the attributes in the database,
    and returns the pks of the attributes.
    """
    # do something
    for i in range(5):
        time.sleep(1)
        print("sleeping", str(i+1))
    # do something nice
    # raise NotImplementedError