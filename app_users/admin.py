""" users models admin """

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app_organizations.admin import Companyinline

# Models
from app_users.models import User
class CustomUserAdmin(UserAdmin):
    """ User Model Admin """
    list_display = ['id','email','username','last_name','is_staff','is_client','is_verified', 'current_site', 'current_organization','owns']
    list_filter = ['is_client','is_staff', 'company', 'created_at']
    ordering = ['id']
    inlines = [
        Companyinline
    ]
    def owns(self, object):
        return object.company.name

admin.site.register(User,CustomUserAdmin)
