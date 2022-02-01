# Django
from django.db import models

# Utilities
from config.utils.models import CustomBaseModel

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
    device_type = models.CharField(max_length=100, choices=VARIABLE_CHOICES)

    # most brands will have some sort of id you'll want to track
    manufacturer_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return '{}'.format(self.id)