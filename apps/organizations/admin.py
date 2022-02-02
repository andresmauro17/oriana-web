from django.contrib import admin

from apps.organizations.models.organization import Organization
from apps.organizations.models import Organization
from apps.organizations.models import Company

class MembershipInline(admin.TabularInline):
    model = Organization.members.through
    # autocomplete_fields=["membership_email"]
    extra = 0
    can_delete = True
    show_change_link = True
    # raw_id_fields = ("user",)
    autocomplete_fields = ['user']

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['id','name','owner']
    autocomplete_fields = ['owner']
    list_editable = []
    list_filter = ['name']
    search_fields = ['id', 'name']
    ordering = ['name','-id']
    inlines = [
        MembershipInline,
    ]

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id','name','comercial_name','id_number','owner']
    autocomplete_fields = ['owner']
    list_editable = []
    list_filter = ['name']
    search_fields = ['id', 'name']
    ordering = ['name','-id']
