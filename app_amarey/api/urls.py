""" App sensors api urls"""

# django imports
# from django.urls import inlcude
from django.urls import path
from rest_framework.routers import DefaultRouter

# views
from app_amarey.api import views as app_data_api_views

router = DefaultRouter()
# router.register(r'', views.SensorViewSet, basename='legacy')

urlpatterns = [
    # path('', include(router.urls)),
    path("<str:sensor_unique>/data/", app_data_api_views.get_sensor_data),
    path("<str:sensor_unique>/data/", app_data_api_views.get_sensor_data),
    path(
        '<str:sensor_unique>/certificates/',
        app_data_api_views.sensor_certificates_view
    )
]
