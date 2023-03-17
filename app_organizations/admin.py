from django.contrib import admin

from app_organizations.models.organization import Organization
from app_organizations.models import Organization
from app_organizations.models import Company
from app_organizations.models import Site

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
    list_display = ['id','name','owner','company_name']
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

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id','name','comercial_name','id_number','owner']
    autocomplete_fields = ['owner']
    list_editable = []
    list_filter = ['name']
    search_fields = ['id', 'name']
    ordering = ['name','-id']
