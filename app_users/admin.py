""" users models admin """

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from app_users.models import User
class CustomUserAdmin(UserAdmin):
    """ User Model Admin """
    list_display = ['id','email','username','last_name','is_staff','is_client','is_verified', 'current_site', 'current_organization']
    list_filter = ['is_client','is_staff','created_at','updated_at']
    ordering = ['id']

admin.site.register(User,CustomUserAdmin)
