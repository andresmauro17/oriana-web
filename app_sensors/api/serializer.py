""" sensor api serializer """

from rest_framework import serializers
from app_sensors.models import Sensor

class CurrentDataSerializer(serializers.Serializer):
    sensortype = serializers.ChoiceField(Sensor.VARIABLE_CHOICES)
    deviceid = serializers.CharField(max_length=100)
    value = serializers.DecimalField(max_digits=5, decimal_places=2)
    energy = serializers.BooleanField()
    datetime = serializers.DateTimeField()

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'
