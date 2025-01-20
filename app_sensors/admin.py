""" Appsensor admin module """
# django imports
from django.contrib import admin

# other apps
# from app_data.admin import DataInline

# local import
from .models import Sensor
from .models import Device
from .models import SensorUserAlarm
from .models import Certificate


class SensorInline(admin.TabularInline):
    """ Sersor inline admin"""
    model = Sensor
    # autocomplete_fields=["membership_email"]
    extra = 0
    can_delete = True
    show_change_link = True
    # raw_id_fields = ("user",)
    # autocomplete_fields = ['name']


class SensorUserAlarmInline(admin.TabularInline):
    """ User alarm inline admin """
    model = SensorUserAlarm
    autocomplete_fields = ["user"]
    extra = 0
    can_delete = True
    show_change_link = True
    # raw_id_fields = ("user",)
    # autocomplete_fields = ['name']


class CertificatesInline(admin.TabularInline):
    """CertificatesInline"""
    model = Certificate
    can_delete = True
    show_change_link = True
    extra = 0


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    """Certificate Admin"""

    list_display = ['id', 'sensor', 'calibration_date', 'url', 'created_at']
    ordering = ['id']
    list_filter = ["sensor"]


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    """ Serson admin """
    list_display = [
        "id",
        "name",
        "unique_id",
        "is_active",
        "sensor_type",
        "last_broker",
        "site",
    ]
    autocomplete_fields = ["site"]
    list_editable = ["name", "unique_id", "sensor_type"]
    list_filter = ["sensor_type", "last_broker", "site"]
    search_fields = ["unique_id", "name"]
    ordering = []
    inlines = [SensorUserAlarmInline, CertificatesInline]


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    """ Device admin """
    list_display = [
        "id",
        "device_id",
        "manufacturing_batch",
        "device_version",
        "notes",
    ]
    list_filter = ["device_version"]
    search_fields = ["device_id"]
    ordering = []
    # inlines = [SensorUserAlarmInline, CertificatesInline]