from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('api/dashboard/', include('app_dashboard.api.urls')),
]