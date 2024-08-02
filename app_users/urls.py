""" users urls """

from django.shortcuts import redirect
from django.urls import include, path

from app_users import views

urlpatterns = [
    path(
        route="login/",
        view=lambda request: redirect("/accounts/login/"),
        name="login",
    ),
    path(route="accounts/login/", view=views.login_view),
    path(
        route="accounts/password-reset/",
        view=views.PasswordResetView.as_view(),
        name="password_reset",
    ),
    path(
        route="accounts/password-reset/done/",
        view=views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        route="accounts/reset/<uidb64>/<token>/",
        view=views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(route="logout/", view=views.logout_view, name="logout"),
    path("api/users/", include("app_users.api.urls")),
]
