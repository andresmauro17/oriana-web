""" Organization Models"""

import random
import os

# Django imports
from django.db import models
from django.conf import settings

# Utilities
from config.utils.models import CustomBaseModel
from apps.organizations.utils.roles import Roles

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "organizations/{organization_id}/{final_filename}".format(
            organization_id=instance.organization.id, 
            final_filename=final_filename
        )

class Organization(CustomBaseModel):
    """
        A user's organizations
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to=upload_image_path, blank=True, null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='organization', blank=True, null=True, on_delete=models.SET_NULL)
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='organizations', through='Membership'
    )

class Membership(CustomBaseModel):
    """
    A user's organizations membership
    """
    id = models.AutoField(primary_key=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, choices=Roles.ROLE_CHOICES, blank=True, null=True, default=Roles.ROLE_CHOICES[1][1])
    class Meta:
        unique_together = (('organization','user'),)