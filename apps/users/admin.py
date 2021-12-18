""" users models admin """

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from apps.users.models import User
class CustomUserAdmin(UserAdmin):
    """ User Model Admin """
    list_display = ('email','username','last_name','is_staff','is_client','is_verified')
    list_filter = ('is_client','is_staff','created_at','updated_at')

admin.site.register(User,CustomUserAdmin)
