""" sensor api serializer """

from decimal import Decimal

from rest_framework import serializers
from app_sensors.models import Sensor
from app_sensors.models import Certificate


class CurrentDataSerializer(serializers.Serializer):
    """ Serializer to get the sensor current data for mqtt"""
    # variable = serializers.ChoiceField(Sensor.VARIABLE_CHOICES)
    deviceid = serializers.CharField(max_length=100)
    value = serializers.DecimalField(max_digits=5, decimal_places=2)
    energy = serializers.BooleanField()
    # datetime = serializers.DateTimeField()
    # date = serializers.DateField()
    # time = serializers.TimeField()


class SensorSerializer(serializers.ModelSerializer):
    """ Sensor serializer"""
    max_threshold = serializers.DecimalField(
        max_digits=4, decimal_places=2, coerce_to_string=False
    )
    min_threshold = serializers.DecimalField(
        max_digits=4, decimal_places=2, coerce_to_string=False
    )
    last_value = serializers.DecimalField(
        max_digits=5, decimal_places=2, coerce_to_string=False
    )
    legacy = serializers.SerializerMethodField()
    location = serializers.SerializerMethodField()

    class Meta:
        """ meta class """
        model = Sensor
        fields = "__all__"

    def get_legacy(self, obj):
        """ legacy flag is always False """
        return False

    def get_location(self, obj):
        """ get the sensor location """
        return obj.get_location


def convert_decimals(data):
    """
        DRF, has issues passing data serialized to django templates, 
        the decimal fields is showed as string, this definition, converts all 
        to float
    """
    for key, value in data.items():
        if isinstance(value, Decimal):
            data[key] = float(value)
    return data


class CertificatesSerializer(serializers.ModelSerializer):
    """ Certificate model serializer"""
    class Meta:
        """ meta class """
        model = Certificate
        fields = "__all__"
