from rest_framework import serializers
from app_amarey.models import Nevera

class NeveraSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='idnevera')
    max_threshold = serializers.FloatField(source='temmax')
    min_threshold = serializers.FloatField(source='temmin')
    last_value = serializers.DecimalField(source='ultimodato', max_digits=8, decimal_places=2)
    name = serializers.CharField(source='nombrenevera')
    sensor_type = serializers.CharField(source='tiposensor')
    last_broker = serializers.CharField(default="emqx")  # Assuming a default value, modify as needed
    unique_id = serializers.CharField(source='sensor')
    is_active = serializers.BooleanField(source='activa')
    was_modified = serializers.BooleanField(source='modificado')
    device_id = serializers.CharField(source='numactivo')
    last_energy_state = serializers.BooleanField(source='ultimodatoenergia')
    last_value_date = serializers.DateField(source='ultimodatofecha')
    last_value_time = serializers.TimeField(source='ultimodatohora')
    site = serializers.PrimaryKeyRelatedField(source='empresa', read_only=True)
    alarms = serializers.SerializerMethodField()
    legacy = serializers.SerializerMethodField()

    class Meta:
        model = Nevera
        fields = [
            'id', 'max_threshold', 'min_threshold', 'last_value',
            'created_at', 'updated_at', 'name', 'sensor_type', 'last_broker',
            'unique_id', 'is_active', 'was_modified', 'device_id', 'last_energy_state',
            'last_value_date', 'last_value_time', 'site', 'alarms','legacy'
        ]

    def get_alarms(self, obj):
        return [obj.temmax, obj.temmin]
    def get_legacy(self, obj):
        return True