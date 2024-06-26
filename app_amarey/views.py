from django.shortcuts import render
from django.shortcuts import get_object_or_404


# Create your views here.
from .api.serializer import NeveraSerializer, convert_decimals
from .models import Nevera

def sensor_home(request, sensor_id):
    nevera = get_object_or_404(Nevera, idnevera=sensor_id)
    nevera_serialized = NeveraSerializer(nevera)
    print(convert_decimals(nevera_serialized.data))
    return render(request, 'app_amarey/sensorlegacy_home.html', {"sensor_serialized":convert_decimals(nevera_serialized.data)})