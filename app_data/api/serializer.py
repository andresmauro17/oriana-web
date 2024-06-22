""" data api serializer """

from rest_framework import serializers
from app_data.models import Data



class DataSerializer(serializers.ModelSerializer):
    value = serializers.DecimalField(max_digits=5, decimal_places=2, coerce_to_string=False)
    class Meta:
        model = Data
        fields = '__all__'
