""" App sensors urls"""

# django imports
from django.urls import include, path

from . import views

urlpatterns = [
    path('sensors/<int:sensor_id>', views.sensor_home, name='sensor_home'),
    path('api/sensors/', include('app_sensors.api.urls'))
]