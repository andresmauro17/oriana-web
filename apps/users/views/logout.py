from django.contrib.auth import logout as logout_django
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def logout_view(request):
    logout_django(request)
    return redirect('users:login')