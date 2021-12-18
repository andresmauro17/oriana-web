""" users urls """

from django.urls import path

from apps.users import views as users_views

urlpatterns = [
    path(
        route='login',
        view=users_views.login_view,
        name="login"
    ),
]
