# Generated by Django 4.2.13 on 2025-01-19 00:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_sensors', '0016_remove_sensor_device'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='device',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='data', to='app_sensors.device'),
        ),
    ]
