# Generated by Django 3.2.10 on 2022-02-02 03:23

import apps.organizations.models.organization
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='role',
            field=models.CharField(blank=True, choices=[('USUARIO', 'usuario'), ('ADMIN', 'administrador')], default='administrador', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=apps.organizations.models.organization.upload_image_path),
        ),
    ]
