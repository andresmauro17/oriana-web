# Generated by Django 3.2.10 on 2023-03-18 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_organizations', '0004_auto_20230318_1647'),
        ('app_sensors', '0002_auto_20230318_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sensor', to='app_organizations.site'),
        ),
    ]
