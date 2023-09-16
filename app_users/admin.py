""" users models admin """

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app_organizations.admin import Companyinline

# Models
from app_users.models import User
class CustomUserAdmin(UserAdmin):
    """ User Model Admin """
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal Information', {'fields': ('profile_image','first_name','last_name', 'phone_number','current_site', 'current_organization')}),
        ('Permissions', {'fields': ('is_active', 'is_verified', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ['id','email','username','last_name','is_staff','is_client','is_verified', 'current_site', 'current_organization','owns']
    list_filter = ['is_client','is_staff', 'company', 'created_at']
    ordering = ['id']
    inlines = [
        Companyinline
    ]
    def owns(self, object):
        return object.company.name

admin.site.register(User,CustomUserAdmin)
