# Django
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Tasks
from app_tasks.tasks import test_task

# Create your views here.
# @login_required
def vue_test(request):
    return render(request, 'sensors/sensors.html')

# @login_required
def test_celery(request):
    test_task.delay()
    return HttpResponse("task executed correctly!")