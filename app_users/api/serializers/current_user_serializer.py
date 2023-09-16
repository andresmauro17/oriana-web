# Rest Framework
from rest_framework import serializers
from app_organizations.api.serializers import organization_serializer

# Local imports
from app_users.models import User

class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)
