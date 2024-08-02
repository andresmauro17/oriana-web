from django.contrib.auth import password_validation
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.views import (
    PasswordResetConfirmView as DjangoPasswordResetConfirmView,
)
from django.contrib.auth.views import (
    PasswordResetDoneView as DjangoPasswordResetDoneView,
)
from django.contrib.auth.views import (
    PasswordResetView as DjangoPasswordResetView,
)
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from app_users.models import User


def login_view(request):
    """Custom login view"""
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("dashboard:dashboard")
        else:
            return render(
                request,
                "app_users/authentication/login.html",
                {"error": "Usuario o clave inválida. ¡Inténtalo de nuevo!"},
            )
    return render(request, "app_users/authentication/login.html")


class PasswordResetView(DjangoPasswordResetView):
    """password reset view form django authentication views"""

    email_template_name = "app_users/authentication/password_reset_email.html"
    html_email_template_name = (
        "app_users/authentication/password_reset_email.html"
    )
    success_url = reverse_lazy("users:password_reset_done")
    template_name = "app_users/authentication/password_reset_form.html"


class PasswordResetDoneView(DjangoPasswordResetDoneView):
    template_name = "app_users/authentication/forget_password_done.html"


class PasswordResetConfirmView(DjangoPasswordResetConfirmView):
    template_name = "app_users/authentication/password_reset_confirm.html"
    success_url = reverse_lazy("users:login")

    def get_context_data(self, **kwargs):
        help_text = password_validation.password_validators_help_texts()
        context = super().get_context_data(**kwargs)
        context["help_text"] = help_text
        return context


@login_required
def logout_view(request):
    # logout a user
    logout(request)
    return redirect("users:login")
