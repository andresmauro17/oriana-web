# django imports
from django.contrib import admin

# local import
from apps.observations.models import Attribute

@admin.register(Attribute)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['id', 'valid_at', 'value', 'units']
    list_editable = []
    list_filter = []
    search_fields = []
    ordering = []
