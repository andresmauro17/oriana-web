"""
app_data_api_views
"""
from datetime import datetime

# restframework imports
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Local imports 
from .serializer import DataSerializer
from app_sensors.models import Sensor

@api_view(['GET'])
def get_sensor_data(request, sensor_unique):
    """
        get the sensor data filterd by date, the url format:
        api/sensors/11/data/?from=2023-08-04&to=2023-08-04
    """
    sensor = Sensor.objects.filter(id=sensor_unique).first()
    if not sensor:
        content = {'message': 'Sensor not found'}
        return Response(content, status=status.HTTP_404_NOT_FOUND)
    
    from_date = request.query_params.get('from')
    to_date = request.query_params.get('to')

    if from_date is None or to_date is None:
        from_date = datetime.today().strftime('%Y-%m-%d')
        to_date = from_date

    from_datetime = datetime.strptime(from_date, '%Y-%m-%d')
    to_datetime = datetime.strptime(to_date, '%Y-%m-%d')
    from_datetime = from_datetime.replace(hour=0, minute=0, second=0)
    to_datetime = to_datetime.replace(hour=23, minute=59, second=59)

    data = sensor.data.filter(
        date__gte=from_datetime,
        date__lte=to_datetime
    ).order_by('date', 'time')
    
    # data = sensor.data.all()
    # print(data)
    serializer = DataSerializer(data, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)
