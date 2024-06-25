from django.shortcuts import redirect
from app_organizations.models import Site, Organization

class VerifyUserHasOrganizationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        response = self.get_response(request)
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        # print("-----------------------------------")
        url = request.get_full_path()
        exclude_urls = ["/api/","/organizations/mising/", "/sites/mising/", "/admin"]
        exclude = False
        for url_to_exclude in exclude_urls:
            if url_to_exclude in url:
                exclude=True
        current_user = request.user
        if not exclude and current_user.is_authenticated:
            organizations = current_user.organizations.all()
            if organizations:
                pass
                # if not current_user.current_organization:
                #     current_user.current_organization = organizations.first()
                # sites = Site.objects.filter(organization=current_user.current_organization)
                # if sites:
                #     current_user.current_site = sites.first()
                # else:
                #     return redirect('organizations:misingsites')
            else:
                return redirect('organizations:misingorganization')
               
        return response