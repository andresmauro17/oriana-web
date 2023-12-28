""" api sensors view"""

# restframework imports
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Local imports 
from .serializer import CurrentDataSerializer, SensorSerializer
from app_sensors.models import Sensor

# apps import
from app_sensors.models import Sensor
from app_data.models import Data

class SensorViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """ Sensor viewset """
    queryset = Sensor.objects.all()
    serializer_class=SensorSerializer
    permission_classes = (IsAuthenticated,)


@api_view(['POST'])
def sensor_data_view(request, sensor_unique):
    """ this endpoint is called by the mqtt broker to store the current data
        request : /api/sensors/fff45524/currentdata/
        {
            "sensortype": "TEMPERATURE",
            "deviceid":"gtv51-l001-l002",
            "value":32,
            "energy":1,
            "datetime":"23-03-29 03:24:00"
        }
    """
    sensor = Sensor.objects.filter(unique_id=sensor_unique).first()
    if not sensor:
        content = {'message': 'Sensor not found'}
        return Response(content, status=status.HTTP_404_NOT_FOUND)
    serializer = CurrentDataSerializer(data = request.data)
    
    serializer.is_valid(raise_exception=True)
    data_created = Data.objects.create(
        sensor = sensor,
        value = serializer.validated_data['value'],
        energy = serializer.validated_data['energy'],
        date = serializer.validated_data['date'],
        time = serializer.validated_data['time'],
    )
    if sensor.sensor_type != serializer.validated_data['sensortype'] or sensor.device_id != serializer.validated_data['deviceid']:
        sensor.sensor_type = serializer.validated_data['sensortype']
        sensor.device_id = serializer.validated_data['deviceid']
        sensor.save()
    sensor_serialized = SensorSerializer(sensor)

    return Response({'data':serializer.validated_data,'sensor':sensor_serialized.data})