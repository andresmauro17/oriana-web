""" syncsensorjsonrules """
from django.core.management.base import BaseCommand
from django.db.models import Q

from app_emqx.services.sensor_services import (
    create_sensor_rule, delete_sensor_rule
)
from app_sensors.models import Sensor


class Command(BaseCommand):
    """
    this command creates all the sensors in the
    python manage.py syncsensorjsonrules
    docker-compose run --rm django python manage.py syncsensorjsonrules
    """

    help = "this command creates the resources in emqx"

    def handle(self, *args, **options):
        """ handle method """
        self.stdout.write(
            self.style.SUCCESS("creating sensors in emqx")
        )
        sensors = Sensor.objects.filter(
            is_active=True,
            is_unknow=False,
            device__isnull=False
        )
        for sensor in sensors:
            response = create_sensor_rule(sensor)
            if response.status_code == 200:
                self.stdout.write(
                    self.style.SUCCESS(f'sensor {sensor} ok')
                )
        
        # deleting the sensors that are not active
        self.stdout.write(
            self.style.ERROR("deleting sensors in emqx that are not active")
        )
        sensors = Sensor.objects.filter(
            Q(is_active=False) |
            Q(is_unknow=True) |
            Q(device__isnull=True)
        )
        for sensor in sensors:
            status_code = delete_sensor_rule(sensor)
            self.stdout.write(
                self.style.ERROR(f'sensor {sensor} ok {status_code}')
            )