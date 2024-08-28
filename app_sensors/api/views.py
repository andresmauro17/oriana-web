""" api sensors view"""

from pytz import timezone
from datetime import datetime

# restframework imports
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Local imports
from app_data.models import Data
from app_sensors.models import Sensor, Certificate
from .serializer import (
    CurrentDataSerializer,
    SensorSerializer,
    CertificatesSerializer,
)


class SensorViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """Sensor viewset"""

    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    permission_classes = (IsAuthenticated,)


@api_view(["POST"])
def sensor_data_view(request, sensor_unique):
    """this endpoint is called by the mqtt broker to store the current data
    request : /api/sensors/fff45524/currentdata/
    {
        "variable": "TEMPERATURE",
        "deviceid":"gtv51-l001-l002",
        "value":32,
        "energy":1,
        "datetime":"23-03-29 03:24:00"
    }
    """
    serializer = CurrentDataSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    sensor = Sensor.objects.filter(unique_id=sensor_unique).first()
    if not sensor:
        Sensor.objects.create(
            name="anonymous",
            sensor_type=serializer.validated_data["variable"],
            last_broker="emqx",
            unique_id=sensor_unique,
            max_threshold=8,
            min_threshold=2,
            is_active=True,
        )
        content = {"message": "Sensor not found"}
        return Response(content, status=status.HTTP_404_NOT_FOUND)

    user_tz = timezone("America/Bogota")
    current_datetime_utc = datetime.now()
    current_datetime_local = current_datetime_utc.astimezone(user_tz).replace(
        tzinfo=None
    )

    data_created = Data.objects.create(
        sensor=sensor,
        value=serializer.validated_data["value"],
        energy=serializer.validated_data["energy"],
        # date=serializer.validated_data["date"],
        # time=serializer.validated_data["time"],
        date=current_datetime_local.date(),
        time=current_datetime_local.time().replace(microsecond=0),
    )
    sensor.last_energy_state = data_created.energy
    sensor.last_value = data_created.value
    sensor.last_value_date = data_created.date
    sensor.last_value_time = data_created.time

    if (
        sensor.sensor_type != serializer.validated_data["variable"]
        or sensor.device_id != serializer.validated_data["deviceid"]
    ):
        sensor.sensor_type = serializer.validated_data["variable"]
        sensor.device_id = serializer.validated_data["deviceid"]

    sensor.save()
    sensor_serialized = SensorSerializer(sensor)

    return Response(
        {"data": serializer.validated_data, "sensor": sensor_serialized.data}
    )


@api_view(["GET"])
def sensor_certificates_view(request, sensor_unique):
    """sensor certificates api view"""
    certificates = Certificate.objects.filter(sensor=sensor_unique).order_by(
        "-calibration_date"
    )
    certificates_serialized = CertificatesSerializer(certificates, many=True)
    return Response({"data": certificates_serialized.data})
