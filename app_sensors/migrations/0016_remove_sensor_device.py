# Generated by Django 4.2.13 on 2025-01-19 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_sensors', '0015_remove_sensor_device_id_sensor_device'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensor',
            name='device',
        ),
    ]
