
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
            return redirect('dashboard:dashboard_site', request.user.current_site.id)

    return render(request, 'dashboard/dashboard.html')

@login_required
def dashboard_site(request, site_id):
    """ this view renderize a tempalte to load the Dashboard component"""
    site = get_object_or_404(Site, pk=site_id)
    return render(request, 'dashboard/dashboard.html', {"site":site})