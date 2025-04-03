"""
app_data_api_views
"""
from datetime import datetime, timedelta
from django.db.models import Q, F, ExpressionWrapper, DurationField, Window
from django.db.models.functions import Abs, TruncHour
from django.db.models.functions.window import Rank

# restframework imports
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Local imports
from app_amarey.models import Nevera
from app_amarey.models import Certificados
from .serializer import DatosSerializer, CertificatesSerializer


@api_view(['GET'])
def get_sensor_data(request, sensor_unique):
    """
    get the sensor data filterd by date, the url format:

    URL format:

    filtering by dates:
    /api/sensorslegacy/643/data/?from=2025-03-25&to=2025-03-26

    filtering by dates but one sample every hour:
    /api/sensorslegacy/643/data/?from=2025-03-25&to=2025-03-26&hourly=true

    filtering by date and get 1 data in a closest time, one sample by day
    /api/sensorslegacy/643/data/?from=2025-03-25&to=2025-03-26&time=07:00:00&time2=17:00:00
    /api/sensorslegacy/643/data/?from=2025-03-25&to=2025-03-26&time1=07:00:00&time2=17:00:00

    filtering by date and get 2 data in two closest time, two sample by day
    /api/sensorslegacy/643/data/?from=2025-03-25&to=2025-03-26&time1=07:00:00&time2=17:00:00


    """
    nevera = Nevera.objects.filter(idnevera=sensor_unique).first()
    if not nevera:
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

    data = nevera.datos.filter(
        fecha__gte=from_datetime,
        fecha__lte=to_datetime
    )

    # Check if the user requested hourly data
    hourly = request.query_params.get('hourly')

    if hourly:
        data = data.annotate(
            hour_group=TruncHour('hora'),  # Truncate to the hour
            rank=Window(expression=Rank(), partition_by=[F("fecha"), F("hour_group")], order_by=[F("hora").asc()])
        ).filter(rank=1)

    # Time filtering
    time_alone = request.query_params.get('time')
    time1 = request.query_params.get('time1')
    time2 = request.query_params.get('time2')

    if not time1 and time_alone:
        time1 = time_alone

    # if only exist one time use the same logic for both times
    if not time2:
        time2 = time1

    if time1 and time2 and not hourly:
        print(f"Filtering data between {time1} and {time2}")
        try:
            time1 = datetime.strptime(time1, '%H:%M:%S').time()
            time2 = datetime.strptime(time2, '%H:%M:%S').time()
        except ValueError:
            return Response({'message': 'Invalid time format, use HH:MM:SS'}, status=status.HTTP_400_BAD_REQUEST)

        # Annotate the absolute difference for each record
        data = data.annotate(
            diff_time1=ExpressionWrapper(Abs(F("hora") - time1), output_field=DurationField()),
            diff_time2=ExpressionWrapper(Abs(F("hora") - time2), output_field=DurationField()),
            rank_time1=Window(expression=Rank(), partition_by=[F("fecha")], order_by=[F("diff_time1").asc()]),
            rank_time2=Window(expression=Rank(), partition_by=[F("fecha")], order_by=[F("diff_time2").asc()])
        ).filter(
            Q(rank_time1=1) | Q(rank_time2=1)
        )
    data = data.order_by("fecha", "hora")

    serializer = DatosSerializer(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(["GET"])
def sensor_certificates_view(request, sensor_unique):
    """sensor certificates api view"""
    certificates = Certificados.objects.filter(nevera=sensor_unique).order_by(
        "-fechacalibracion"
    )
    certificates_serialized = CertificatesSerializer(certificates, many=True)
    return Response({"data": certificates_serialized.data})
