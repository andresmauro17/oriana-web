""" api dashboard view"""

# restframework imports
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

#local import
from app_sensors.models import Sensor
from app_organizations.models import Site
from app_sensors.api.serializer import SensorSerializer

@api_view(["GET"])
def dahsboard_sensors(request, site_id):
    try:
        site = Site.objects.get(pk=site_id)
    except:
        return Response({"message":"not found"},status=status.HTTP_404_NOT_FOUND)
    data = {"hello":"world"}
    sensors = Sensor.objects.filter(site=site)
    serializer = SensorSerializer(sensors, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)