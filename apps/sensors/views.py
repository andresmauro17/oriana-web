from django.shortcuts import render
from django.http import HttpResponse

# Tasks
from apps.taskapp.tasks import test_task

# Create your views here.
def vue_test(request):
    return render(request, 'sensors/sensors.html')

def test_celery(request):
    test_task.delay()
    return HttpResponse("task executed correctly!")