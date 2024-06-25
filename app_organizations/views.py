
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
    if organization_id==0:
        current_user.current_organization = None
        current_user.current_site = None
    else:
        organization = get_object_or_404(Organization,pk=organization_id)
        current_user.current_organization = organization
        sites = Site.objects.filter(organization=organization)
        if sites:
            current_user.current_site = sites.first()
    current_user.save()
    
    return redirect('dashboard:dashboard_site', current_user.current_site.id)

@login_required
def switch_site(request, site_id):
    """ this view switch organizations"""
    current_user = request.user
    site = get_object_or_404(Site,pk=site_id)
    current_user.current_site = site
    current_user.save()
    
    return redirect('dashboard:dashboard_site', current_user.current_site.id)

@login_required
def misingorganization(request):
    current_user = request.user
    organizations = current_user.organizations.all()
    if(organizations):
        return redirect('dashboard:dashboard_site', current_user.current_site.id)
    return render(request, "app_organizations/misingorganization.html")

@login_required
def misinsites(request):
    return render(request, "app_organizations/misinsites.html")