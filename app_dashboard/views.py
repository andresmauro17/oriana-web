"""
    Dashboard view
"""

from datetime import datetime

# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from pytz import timezone

from app_amarey.models import Nevera
from app_organizations.models import Site
from app_sensors.models import Sensor

# Create your views here.


@login_required
def dashboard(request):
    """this view renderize a tempalte to load the Dashboard component"""

    if request.user.current_site:
        return render(
            request,
            "dashboard/dashboard.html",
            {"site": request.user.current_site},
        )

    return render(request, "dashboard/dashboard.html", {"site": {"id": 0}})


@login_required
def dashboardStatus(request):
    """this view renderize an status of all the current sensors"""
    hour_treshold = 2
    user_tz = timezone("America/Bogota")
    current_datetime_utc = datetime.now()
    current_datetime_local = current_datetime_utc.astimezone(user_tz).replace(
        tzinfo=None
    )
    current_datetime_local_str = current_datetime_local.strftime(
        "%Y-%m-%d %H:%M:%S %Z"
    )

    includedeactivated = request.GET.get("includedeactivated")
    site = request.user.current_site
    if site:
        sites_ids = [site.id]
    else:
        if request.user.current_organization:
            sites_ids = Site.objects.filter(
                organization=request.user.current_organization
            )
        else:
            organizations_ids = (
                request.user.get_user_organizations.values_list(
                    "id", flat=True
                )
            )
            sites_ids = Site.objects.filter(
                organization_id__in=organizations_ids
            ).values_list("id", flat=True)

    sites = (
        Site.objects.get_active()
        .filter(id__in=sites_ids)
        .order_by("organization")
    )

    sensors = Sensor.objects.filter(site_id__in=sites_ids)
    if not includedeactivated:
        sensors = sensors.filter(is_active=True)

    sensors_by_site = {}
    for sensor in sensors:
        hours_delayed = 0
        is_delayed = False
        if sensor.last_value_date_time:
            diff = current_datetime_local - sensor.last_value_date_time
            hours_delayed = round(diff.total_seconds() / 3600)
            if hours_delayed > hour_treshold:
                is_delayed = True
        sensor.is_delayed = is_delayed
        sensor.hours_delayed = hours_delayed

        if sensor.site_id not in sensors_by_site:
            sensors_by_site[sensor.site_id] = []
        sensors_by_site[sensor.site_id].append(sensor)

    # Legacy database
    empresas_ids = (
        Site.objects.filter(id__in=sites_ids)
        .exclude(empresa_id_amarey__isnull=True)
        .values_list("empresa_id_amarey", flat=True)
    )
    # filtered_empresas_ids = [id for id in empresas_ids if id is not None]
    legacy_sensors = Nevera.objects.filter(empresa_id__in=list(empresas_ids))
    if not includedeactivated:
        legacy_sensors = legacy_sensors.get_active()

    neveras_by_site = {}
    for nevera in legacy_sensors:
        hours_delayed = 0
        is_delayed = False
        if nevera.ultimodatetime:
            diff = current_datetime_local - nevera.ultimodatetime
            hours_delayed = round(diff.total_seconds() / 3600)
            if hours_delayed > hour_treshold:
                is_delayed = True
        nevera.is_delayed = is_delayed
        nevera.hours_delayed = hours_delayed

        if nevera.empresa_id not in neveras_by_site:
            neveras_by_site[nevera.empresa_id] = []
        neveras_by_site[nevera.empresa_id].append(nevera)

    # Create the final list of dictionaries
    sitesdicts = []
    for site in sites:
        site_dict = {
            "get_site_org": site.get_site_org,
            "id": site.id,
            "sensors": sensors_by_site.get(site.id, []),
            "legacy_sensors": neveras_by_site.get(site.empresa_id_amarey, []),
        }
        sitesdicts.append(site_dict)

    sites = sitesdicts
    # print(type(sites[0]["legacy_sensors"][0].temmax))

    return render(
        request,
        "dashboard/status.html",
        {
            "current_datetime_local": current_datetime_local_str,
            "sites": sites,
            "hour_treshold": hour_treshold,
        },
    )
