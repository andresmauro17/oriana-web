# Generated by Django 3.2.10 on 2023-05-19 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]