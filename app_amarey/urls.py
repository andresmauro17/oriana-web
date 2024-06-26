""" App sensors urls"""

# django imports
from django.urls import include, path

from . import views

urlpatterns = [
    path('sensorslegacy/<int:sensor_id>', views.sensor_home, name='sensor_home'),
    path('api/sensorslegacy/', include('app_amarey.api.urls'))
]