""" App sensors urls"""

# django imports
from django.conf.urls import url
from django.urls import include, path

urlpatterns = [
    path('api/sensors/', include('app_sensors.api.urls'))
]