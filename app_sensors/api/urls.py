""" App sensors api urls"""

# django imports
from django.conf.urls import url
from django.urls import path

# views
from .views import sensor_data_view

urlpatterns = [
    path('<str:sensor_unique>/currentdata/', sensor_data_view)
]