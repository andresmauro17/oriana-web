""" api dashboard view"""

# restframework imports
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from django.db.models import Q
#local import
from app_sensors.models import Sensor
from app_organizations.models import Site, Organization
from app_sensors.api.serializer import SensorSerializer
from app_amarey.api.serializer import NeveraSerializer
from app_amarey.models import Empresa, Nevera

@api_view(["GET"])
def dahsboard_sensors(request):
    includedeactivated = request.GET.get('includedeactivated')
    site = request.user.current_site
    if(site):
        sites_ids = [site.id]
    else:
        if request.user.current_organization:
            sites_ids = Site.objects.filter(organization = request.user.current_organization)
        else:
            organizations_ids = request.user.get_user_organizations.values_list('id', flat=True)
            sites_ids = Site.objects.filter(organization_id__in = organizations_ids).values_list('id', flat=True)
    sensors = Sensor.objects.filter(site_id__in=sites_ids)
    if not includedeactivated:
        sensors = sensors.filter(is_active=True)

    #Legacy database 
    empresas_ids = Site.objects.filter(id__in = sites_ids).exclude(empresa_id_amarey__isnull=True).values_list('empresa_id_amarey', flat=True)
    filtered_empresas_ids = [id for id in empresas_ids if id is not None]
    legacy_sensors = Nevera.objects.filter(empresa_id__in = list(empresas_ids))
    if not includedeactivated:
        legacy_sensors = legacy_sensors.filter(activa=True)


    serializer = SensorSerializer(sensors, many=True)
    legacy_serializer = NeveraSerializer(legacy_sensors, many=True)
    return Response(serializer.data + legacy_serializer.data,status=status.HTTP_200_OK)