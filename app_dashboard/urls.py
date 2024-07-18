from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("status/", views.dashboardStatus, name="dashboardStatus"),
    path("api/dashboard/", include("app_dashboard.api.urls")),
]
