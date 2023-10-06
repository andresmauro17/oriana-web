# Django
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# Tasks
from app_tasks.tasks import test_task

# local
from app_sensors.models import Sensor
from .api.serializer import SensorSerializer

# Create your views here.
# @login_required
def vue_test(request):
    return render(request, 'sensors/vue-test.html')

# @login_required
def test_celery(request):
    test_task.delay()
    return HttpResponse("task executed correctly!")


def sensor_home(request, sensor_id):
    sensor = get_object_or_404(Sensor, pk=sensor_id)
    sensor_serialized = SensorSerializer(sensor)
    return render(request, 'sensors/sensor_home.html', {"sensor_serialized":sensor_serialized.data})