# from __future__ import absolute_import
from django.contrib import admin

from app_organizations.models.organization import Organization
from app_organizations.models import Organization
from app_organizations.models import Company
from app_organizations.models import Site
from app_sensors.admin import SensorInline

class MembershipInline(admin.TabularInline):
    model = Organization.members.through
    # autocomplete_fields=["membership_email"]
    extra = 0
    can_delete = True
    show_change_link = True
    # raw_id_fields = ("user",)
    autocomplete_fields = ['user']

class SiteInline(admin.TabularInline):
    model = Site
    # autocomplete_fields=["membership_email"]
    extra = 0
    can_delete = True
    show_change_link = True
    # raw_id_fields = ("user",)
    # autocomplete_fields = ['name']

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['id','name','owner','is_active','company_name']
    autocomplete_fields = ['owner']
    list_editable = []
    list_filter = ['owner__company']
    search_fields = ['id', 'name']
    ordering = ['name','-id',]
    inlines = [
        MembershipInline,
        SiteInline,
    ]

    def company_name(self, obj):
        return obj.owner.company


class Companyinline(admin.StackedInline):
    model = Company
    # autocomplete_fields=["membership_email"]
    extra = 0
    can_delete = True
    show_change_link = True
    # raw_id_fields = ("user",)
    # autocomplete_fields = ['name']

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id','name','comercial_name','id_number','owner']
    autocomplete_fields = ['owner']
    list_editable = []
    list_filter = ['name']
    search_fields = ['id', 'name']
    ordering = ['name','-id']

@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ['id','name','organization']
    autocomplete_fields = ['organization']
    list_editable = []
    list_filter = ['organization']
    search_fields = ['id', 'name']
    ordering = ['id']
    inlines = [SensorInline]

