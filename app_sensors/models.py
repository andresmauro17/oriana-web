""" Sensors related models """

import random

# Django
from datetime import datetime
from django.db import models

# Models
from app_organizations.models import Site
from app_users.models import User

# Utilities
from config.utils.models import CustomBaseModel
from app_utilities.utils import get_filename_ext


class Sensor(CustomBaseModel):
    """Sensor Model.
    This model is the sensors that take the data

    """

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    VARIABLE_CHOICES = (
        ("TEMPERATURE", "Temperatura"),
        ("HUMIDITY", "Humedad"),
    )
    sensor_type = models.CharField(max_length=100, choices=VARIABLE_CHOICES)

    BROKER_CHOICES = (
        ("java", "Java Server"),
        ("emqx", "EMQX"),
    )
    last_broker = models.CharField(max_length=100, choices=BROKER_CHOICES)

    # most brands will have some sort of id you'll want to track
    unique_id = models.CharField(max_length=100, unique=True)
    max_threshold = models.DecimalField(max_digits=4, decimal_places=2)
    min_threshold = models.DecimalField(max_digits=4, decimal_places=2)
    is_active = models.BooleanField(default=True)
    was_modified = models.BooleanField(default=False)
    alarms = models.ManyToManyField(User, through="SensorUserAlarm")
    site = models.ForeignKey(
        Site,
        blank=True,
        null=True,
        related_name="sensor",
        on_delete=models.SET_NULL,
    )
    device_id = models.CharField(max_length=100, blank=True, null=True)
    last_value = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    last_energy_state = models.BooleanField(null=True, blank=True)
    # last_value_date_time = models.DateTimeField(blank=True, null=True)
    last_value_date = models.DateField(blank=True, null=True)
    last_value_time = models.TimeField(blank=True, null=True)

    @property
    def get_location(self):
        """ get location string """
        return f"{self.site.organization.name}|{self.site.name}"

    @property
    def last_value_date_time(self):
        """ get last datetime values """
        if self.last_value_date and self.last_value_time:
            return datetime.combine(self.last_value_date, self.last_value_time)
        return None

    def __str__(self):
        return f"{self.id}"


class SensorUserAlarm(models.Model):
    """Alarms cofiguration model"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    is_email = models.BooleanField()
    is_sms = models.BooleanField()

    class Meta:
        """ meta class """
        unique_together = (("user", "sensor"),)


def upload_cert_path(instance, filename):
    """path to store certs"""
    rand = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = f"{rand}_{name}{ext}"
    return f"certificates/sensor/{instance.sensor.id}/{final_filename}"


class Certificate(CustomBaseModel):
    """calibration certs"""
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    url = models.FileField(upload_to=upload_cert_path, max_length=255)
    calibration_date = models.DateField()