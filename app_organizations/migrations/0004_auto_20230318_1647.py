# Generated by Django 3.2.10 on 2023-03-18 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_organizations', '0003_membership_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='city',
        ),
        migrations.AddField(
            model_name='organization',
            name='city',
            field=models.CharField(default='Cali', max_length=100),
            preserve_default=False,
        ),
    ]