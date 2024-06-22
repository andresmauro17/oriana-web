import random
import os

# django imports
from django.db import models

# Utilities
from config.utils.models import CustomBaseModel

from django.conf import settings

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "companies/{company_id}/{final_filename}".format(
            company_id=instance.company.id, 
            final_filename=final_filename
        )

class Company(CustomBaseModel):
    id = models.AutoField(primary_key=True)
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100, blank=True, null=True)
    comercial_name = models.CharField(max_length=100, blank=True, null=True)
    id_number = models.CharField(max_length=100, blank=True, null=True)
    logo = models.ImageField(upload_to=upload_image_path, blank=True, null=True)

    def __str__(self):
        return self.comercial_name