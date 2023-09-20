""" organizations urls """

from django.urls import path, include
from . import views

urlpatterns = [
    path('organizations/<int:organization_id>/switch/', views.switch_organization, name='switch_organization'),
    path('sites/<int:site_id>/switch/', views.switch_site, name='switch_site'),
    path('api/organizations/',include('app_organizations.api.urls'))
]
