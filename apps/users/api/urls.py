""" users api urls"""
from django.urls import path
from apps.users.api.views import login_view
from apps.users.api.views import user_current_view

urlpatterns = [
    path('login',login_view),
    path('current',user_current_view),
]