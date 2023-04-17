from django.contrib import admin
from app_data.models import Data

@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ['id', 'sensor', 'value', 'energy','date','time']
    # autocomplete_fields = ['sensor']
    # list_editable = ['name','manufacturer_id', 'device_type']
    list_filter = ['sensor']
    search_fields = []
    ordering = []

