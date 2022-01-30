""" users urls """

from django.urls import path, include

from apps.users import views as users_views

urlpatterns = [
    path(
        route='login',
        view=users_views.login_view,
        name="login"
    ),
    path('api/users',include('apps.users.api.urls'))
]
