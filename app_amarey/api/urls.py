""" App sensors api urls"""

# django imports
from django.urls import include, path

from rest_framework.routers import DefaultRouter

# views
from . import views
from app_amarey.api import views as app_data_api_views


router = DefaultRouter()
# router.register(r'', views.SensorViewSet, basename='legacy')

urlpatterns = [
    # path('', include(router.urls)),
    path('<str:sensor_unique>/data/', app_data_api_views.get_sensor_data),
]