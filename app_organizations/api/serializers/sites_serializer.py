from rest_framework import serializers
from app_organizations.models import Site


class SiteModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Site
        fields = '__all__' 