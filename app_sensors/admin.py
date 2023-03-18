from django.contrib import admin

# django imports
from django.contrib import admin

# local import
from app_sensors.models import Sensor
from app_sensors.models import SensorUserAlarm

class SensorInline(admin.TabularInline):
    model = Sensor
    # autocomplete_fields=["membership_email"]
    extra = 0
    can_delete = True
    show_change_link = True
    # raw_id_fields = ("user",)
    # autocomplete_fields = ['name']

class SensorUserAlarmInline(admin.TabularInline):
    model = SensorUserAlarm
    autocomplete_fields=["user"]
    extra = 0
    can_delete = True
    show_change_link = True
    # raw_id_fields = ("user",)
    # autocomplete_fields = ['name']

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'manufacturer_id', 'device_type','site']
    autocomplete_fields = ['site']
    list_editable = ['name','manufacturer_id', 'device_type']
    list_filter = ['device_type', 'site']
    search_fields = []
    ordering = []
    inlines = [ SensorUserAlarmInline ]
