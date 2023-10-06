""" App sensors api urls"""

# django imports
from django.conf.urls import url
from django.urls import include, path

from rest_framework.routers import DefaultRouter

# views
from . import views


router = DefaultRouter()
router.register(r'', views.SensorViewSet, basename='sensor')

urlpatterns = [
    path('', include(router.urls)),
    path('<str:sensor_unique>/currentdata/', views.sensor_data_view)
]