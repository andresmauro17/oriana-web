""" users urls """

from django.urls import path, include

from app_users import views as users_views

urlpatterns = [
    path(route='login', view=users_views.login_view, name="login"),
    path(route='logout', view=users_views.logout_view, name="logout"),
    path('api/users/',include('app_users.api.urls'))
]
