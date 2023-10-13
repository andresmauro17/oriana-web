"""
app_data_api_views
"""

# restframework imports
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Local imports 
from .serializer import DataSerializer
from app_sensors.models import Sensor

@api_view(['GET'])
def get_sensor_data(request, sensor_unique):
    sensor = Sensor.objects.filter(id=sensor_unique).first()
    if not sensor:
        content = {'message': 'Sensor not found'}
        return Response(content, status=status.HTTP_404_NOT_FOUND)
    data = sensor.data.all()
    print(data)
    serializer = DataSerializer(data, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)
