from rest_framework import serializers
from app_organizations.models import Organization
from .sites_serializer import SiteModelSerializer

class OrganizationModelSerializer(serializers.ModelSerializer):
    sites = SiteModelSerializer(many=True, read_only=True)
    class Meta:
        model = Organization
        fields = ['id', 'name', 'logo', 'city', 'owner', 'members', 'sites']