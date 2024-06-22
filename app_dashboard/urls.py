from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('dashboard/<int:site_id>/sensors', views.dashboard_site, name='dashboard_site'),
    path('api/dashboard/', include('app_dashboard.api.urls')),
]