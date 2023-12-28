# Django
from django.db import models

# Utilities
from config.utils.models import CustomBaseModel

# Models
from app_organizations.models import Site
from app_users.models import User



class Sensor(CustomBaseModel):
    """ Sensor Model.
        This model is the sensors that take the data

    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    VARIABLE_CHOICES = (
        ('TEMPERATURE', 'Temperatura'),
        ('HUMIDITY','Humedad'),
    )
    sensor_type = models.CharField(max_length=100, choices=VARIABLE_CHOICES)

    # most brands will have some sort of id you'll want to track
    unique_id = models.CharField(max_length=100, unique=True)
    max_threshold = models.DecimalField(max_digits=4, decimal_places=2)
    min_threshold = models.DecimalField(max_digits=4, decimal_places=2)
    is_active = models.BooleanField(default=True)
    was_modified = models.BooleanField(default=False)
    alarms = models.ManyToManyField(User, through='SensorUserAlarm')
    site = models.ForeignKey(Site, blank=True, null=True,related_name='sensor', on_delete=models.SET_NULL)
    device_id = models.CharField(max_length=100, blank=True, null=True)
    last_value = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    last_energy_state = models.BooleanField(null=True, blank=True)
    # last_value_date_time = models.DateTimeField(blank=True, null=True)
    last_value_date = models.DateField(blank=True, null=True)
    last_value_time = models.TimeField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.id)

class SensorUserAlarm(models.Model):
    """Alarms cofiguration model"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    is_email = models.BooleanField()
    is_sms = models.BooleanField()
    class Meta:
        unique_together = (('user','sensor'),)