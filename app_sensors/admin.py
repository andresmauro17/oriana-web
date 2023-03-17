from django.contrib import admin

# django imports
from django.contrib import admin

# local import
from app_sensors.models import Sensor

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'manufacturer_id', 'device_type','site']
    # autocomplete_fields = ['site']
    list_editable = ['name','manufacturer_id', 'device_type']
    list_filter = ['device_type']
    search_fields = []
    ordering = []
