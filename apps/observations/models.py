# django imports
from django.db import models

# local imports
from apps.sensors.models import Sensor

class BaseAttribute(models.Model):
    
    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which the object was created.'
    )

    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date time on which the object was last modified.'
    )

    # time that the attribute is valid
    # may be different than the time it was created
    # adding the index is important because it's used for sorting
    valid_at = models.DateTimeField(db_index=True)

    # device that's the source of the attribute
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)

    class Meta:
        abstract = True
        get_latest_by = 'valid_at'


class Attribute(BaseAttribute):
    # numerical value of the attribute
    value = models.FloatField()

    # units of the numerical value
    # you may want to add choices to this
    # adding the index is important because it's used for filtering
    units = models.CharField(max_length=10, db_index=True)
