from django.shortcuts import redirect
from app_organizations.models import Site, Organization

class VerifyUserHasOrganizationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        response = self.get_response(request)
        url = request.get_full_path()
    
        exclude = False
        current_user = request.user
        exclude = True if current_user.is_staff else False

        exclude_urls = ["/api/","/organizations/mising/", "/sites/mising/", "/admin"]
        for url_to_exclude in exclude_urls:
            if url_to_exclude in url:
                exclude=True
        
        if not exclude and current_user.is_authenticated:
            organizations = current_user.get_user_organizations
            if organizations:
                pass
            else:
                return redirect('organizations:misingorganization')
               
        return response