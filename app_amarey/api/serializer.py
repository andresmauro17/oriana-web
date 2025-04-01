""" legacy seriliazers """

from decimal import Decimal
from rest_framework import serializers
from app_amarey.models import Nevera, Datos, Certificados


class NeveraSerializer(serializers.ModelSerializer):
    """ Legacy nevera serializer """
    id = serializers.IntegerField(source="idnevera")
    max_threshold = serializers.FloatField(source="temmax")
    min_threshold = serializers.FloatField(source="temmin")
    last_value = serializers.DecimalField(
        source="ultimodato", max_digits=8, decimal_places=2
    )
    name = serializers.CharField(source="nombrenevera")
    last_broker = serializers.CharField(
        default="emqx"
    )  # Assuming a default value, modify as needed
    unique_id = serializers.CharField(source="sensor")
    is_active = serializers.BooleanField(source="activa")
    was_modified = serializers.BooleanField(source="modificado")
    device_id = serializers.CharField(source="numactivo")
    last_energy_state = serializers.BooleanField(source="ultimodatoenergia")
    last_value_date = serializers.DateField(source="ultimodatofecha")
    last_value_time = serializers.TimeField(source="ultimodatohora")
    site = serializers.PrimaryKeyRelatedField(source="empresa", read_only=True)
    alarms = serializers.SerializerMethodField()
    legacy = serializers.SerializerMethodField()
    location = serializers.SerializerMethodField()
    sensor_type = serializers.SerializerMethodField()

    class Meta:
        """ Meta class """
        model = Nevera
        fields = [
            "id",
            "max_threshold",
            "min_threshold",
            "last_value",
            "created_at",
            "updated_at",
            "name",
            "sensor_type",
            "last_broker",
            "unique_id",
            "is_active",
            "was_modified",
            "device_id",
            "last_energy_state",
            "last_value_date",
            "last_value_time",
            "site",
            "alarms",
            "legacy",
            "location",
        ]

    def get_alarms(self, obj):
        """ get alarms formated """
        return [obj.temmax, obj.temmin]

    def get_legacy(self, obj):
        """ this is always a legacy sensor """
        return True

    def get_location(self, obj):
        """ get location """
        return obj.get_location

    def get_sensor_type(self, obj):
        """ nevera type needs to be the same that the sensor is """
        sensortype = None
        if obj.tiposensor == "temperatura":
            sensortype = "TEMPERATURE"
        elif obj.tiposensor == "humedad":
            sensortype = "HUMIDITY"
        return sensortype


class DatosSerializer(serializers.ModelSerializer):
    """ legacy datos seriliazer """
    id = serializers.IntegerField(source="iddatos")
    value = serializers.DecimalField(
        source="temperatura",
        max_digits=6,
        decimal_places=2,
        coerce_to_string=False,
    )
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    energy = serializers.BooleanField(source="energia")
    date = serializers.DateField(source="fecha")
    time = serializers.TimeField(source="hora")
    sensor = serializers.PrimaryKeyRelatedField(
        source="nevera", read_only=True
    )

    class Meta:
        """ meta class """
        model = Datos
        fields = [
            "id",
            "value",
            "created_at",
            "updated_at",
            "energy",
            "date",
            "time",
            "sensor",
        ]

def convert_decimals(data):
    """
    DRF, has issues passing data serialized to django templates,
    the decimal fields is showed as string, this definition,
    converts all to float
    """
    for key, value in data.items():
        if isinstance(value, Decimal):
            data[key] = float(value)
    return data


class CertificatesSerializer(serializers.ModelSerializer):
    """ Certificate model serializer"""
    calibration_date = serializers.DateField(source="fechacalibracion")

    class Meta:
        """ meta class """
        model = Certificados
        fields = "__all__"
