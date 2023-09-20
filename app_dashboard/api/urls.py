""" App sensors api urls"""

# django imports
from django.conf.urls import url
from django.urls import path

# views
from .views import dahsboard_sensors

urlpatterns = [
    path('<int:site_id>/sensors', dahsboard_sensors)
]