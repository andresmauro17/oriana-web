
"""
    Dashboard view
"""

# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from app_organizations.models import Site, Organization

# Create your views here.
@login_required
def switch_organization(request, organization_id):
    """ this view switch organizations"""
    current_user = request.user

    current_user.current_site = None
    if organization_id==0:
        current_user.current_organization = None
    else:
        organization = get_object_or_404(current_user.get_user_organizations, pk=organization_id)
        if(organization):
            current_user.current_organization = organization
    current_user.save()

    previous_url = request.META.get('HTTP_REFERER', 'fallback_url_name')
    return redirect(previous_url)

@login_required
def switch_site(request, site_id):
    """ this view switch organizations"""
    current_user = request.user
    if site_id == 0 or not current_user.current_organization:
        current_user.current_site = None
    else:
        site = get_object_or_404(current_user.current_organization.sites, pk=site_id)
        current_user.current_site = site
    current_user.save()
    
    previous_url = request.META.get('HTTP_REFERER', 'fallback_url_name')
    return redirect(previous_url)

@login_required
def misingorganization(request):
    current_user = request.user
    organizations = current_user.get_user_organizations
    if organizations or current_user.is_staff:
        return redirect('dashboard:dashboard')
    return render(request, "app_organizations/misingorganization.html")

@login_required
def misinsites(request):
    return render(request, "app_organizations/misinsites.html")