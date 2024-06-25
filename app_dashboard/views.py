
"""
    Dashboard view
"""

# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from app_organizations.models import Site

# Create your views here.
@login_required
def dashboard(request):
    """ this view renderize a tempalte to load the Dashboard component"""

    if request.user.current_site:
        return render(request, 'dashboard/dashboard.html',{"site":request.user.current_site})

    return render(request, 'dashboard/dashboard.html',{"site":{"id":0}})