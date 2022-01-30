""" users api urls"""
from django.urls import path
from apps.users.api.views import login_view

urlpatterns = [
    path('/login',login_view),
]