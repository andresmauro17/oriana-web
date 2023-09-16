""" organizations urls """

from django.urls import path, include

urlpatterns = [
    path('api/organizations/',include('app_organizations.api.urls'))
]
