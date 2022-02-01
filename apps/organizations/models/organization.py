""" Organization Model DB"""

# Django imports
from django.db import models
from apps.users.models import User

def upload_image_path(instance, filename):
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "organizations/{organization_id}/{final_filename}".format(
            organization_id=instance.organization.id, 
            final_filename=final_filename
        )

class Organization(models.Model):
    """ Organization Model
        this model is to manage all the tenant
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    photo_url = models.ImageField(upload_to=upload_image_path)
    owner = models.ForeignKey(User,related_name='images', on_delete=models.SET_NULL)
