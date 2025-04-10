# Generated by Django 3.2.10 on 2023-03-18 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_sensors', '0004_alter_sensoruseralarm_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='updated at')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('value', models.DecimalField(decimal_places=2, max_digits=5)),
                ('energy', models.BooleanField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data', to='app_sensors.sensor')),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
    ]
