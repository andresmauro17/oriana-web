""" Sensors related models """

import random

# Django
from datetime import datetime
from django.db import models
from django.db.models.signals import post_save

# Models
from app_organizations.models import Site
from app_users.models import User
from app_emqx.services.sensor_services import (
    create_sensor_rule, delete_sensor_rule
)

# Utilities
from config.utils.models import CustomBaseModel
from app_utilities.utils import get_filename_ext


class Device(CustomBaseModel):
    """Device model"""

    device_id = models.CharField(max_length=100)
    manufacturing_batch = models.CharField(
        max_length=100, blank=True, null=True
    )
    device_version = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.device_id}"


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
    sensor_type = models.CharField(
        max_length=100, choices=VARIABLE_CHOICES, default="TEMPERATURE"
    )
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
    is_unknow = models.BooleanField(default=False)
    site = models.ForeignKey(
        Site,
        blank=True,
        null=True,
        related_name="sensor",
        on_delete=models.SET_NULL,
    )
    device = models.ForeignKey(
        Device,
        related_name="data",
        on_delete=models.SET_NULL,
        db_index=True,
        null=True,
        blank=True,
    )
    last_value = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    last_energy_state = models.BooleanField(null=True, blank=True)
    # last_value_date_time = models.DateTimeField(blank=True, null=True)
    last_value_date = models.DateField(blank=True, null=True)
    last_value_time = models.TimeField(blank=True, null=True)

    def get_contacts(self):
        """
        Retrieve contacts.
        """
        related_alarms = SensorUserAlarm.objects.filter(
            sensor=self
        ).select_related("user")

        sms_numbers = [
            alarm.user.phone_number for alarm in related_alarms if alarm.is_sms
        ]
        emails = [
            alarm.user.email for alarm in related_alarms if alarm.is_email
        ]
        return {
            "sms_numbers": sms_numbers,
            "emails": emails,
        }

    def save(self, *args, **kwargs):
        """
            Save method,the idea is to prevent override updated_at if changes
            the data sensor info and apply was modified if not
        """
        if self.pk:  # Check if is not a new object
            original = Sensor.objects.get(pk=self.pk)
            if (
                original.last_value != self.last_value
                or original.last_energy_state != self.last_energy_state
                or original.last_value_date != self.last_value_date
                or original.last_value_time != self.last_value_time
            ):
                self.updated_at = original.updated_at  # Preserve the original
                self.was_modified = False
            else:
                self.was_modified = True
            
            if self.name != "anonymous":
                self.is_unknow = False
        super(Sensor, self).save(*args, **kwargs)

    @property
    def get_location(self):
        """get location string"""
        if self.site:
            return f"{self.site.organization.name}|{self.site.name}"
        else:
            return ""

    @property
    def last_value_date_time(self):
        """get last datetime values"""
        if self.last_value_date and self.last_value_time:
            return datetime.combine(self.last_value_date, self.last_value_time)
        return None

    def __str__(self):
        return f"{self.id}"


def update_emqx_rule(sender, instance, *args, **kwargs):
    """update_emqx_rule"""
    if (
        instance.is_active
        and not instance.is_unknow
        and instance.device
    ):
        print("creating rule")
        create_sensor_rule(instance)
    else:
        print("delete rule")
        delete_sensor_rule(instance)


post_save.connect(update_emqx_rule, sender=Sensor)


class SensorUserAlarm(models.Model):
    """Alarms cofiguration model"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    is_email = models.BooleanField()
    is_sms = models.BooleanField()

    class Meta:
        """meta class"""

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
