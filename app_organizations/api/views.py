# Django Rest Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# local imports
from app_organizations.models import Organization
from app_organizations.api.serializers import OrganizationModelSerializer

@api_view(["GET"])
def index_view(request):
    organizations = []

    if request.user.is_anonymous:
        return Response(organizations,status=status.HTTP_200_OK)

    if request.user.is_staff:
        organizations = Organization.objects.all()
    else:
        organizations = request.user.organizations.all()
    serializer = OrganizationModelSerializer(organizations, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)