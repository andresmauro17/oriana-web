""" App sensors api urls"""

# django imports
from django.urls import path

# views
from .views import dahsboard_sensors

urlpatterns = [
    path('sensors/', dahsboard_sensors),
]