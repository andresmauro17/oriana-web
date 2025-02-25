"""User model."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.core.validators import RegexValidator
from django.db.models import Q

# Models
from app_organizations.models import Site
from app_organizations.models import Organization

# Utilities
from config.utils.models import CustomBaseModel

class UserManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have an usernale')
        if not first_name:
            raise ValueError('Users must have a first name')
        if not last_name:
            raise ValueError('Users must have a last name')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(CustomBaseModel, AbstractUser):
    """User model.
    Extend from Django's Abstract User, change the username field
    to email and add some extra fields.
    """
    id = models.AutoField(primary_key=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )
    profile_image = models.ImageField(upload_to='profile_images/photo', blank=True, null=True)

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name','last_name','username']

    objects = UserManager()

    is_client = models.BooleanField(
        'client status',
        default=True,
        help_text=(
            'Help easily distinguish users and perform queries. '
            'Clients are the main type of user.'
        )
    )

    is_verified = models.BooleanField(
        'verified',
        default=False,
        help_text=(
            'Set to true when the user have verified its email address.'
        )
    )

    current_organization = models.ForeignKey(Organization, blank=True, null=True, on_delete=models.SET_NULL)
    current_site = models.ForeignKey(Site, blank=True, null=True, on_delete=models.SET_NULL)
    @property
    def get_user_organizations(self):
        "Returns the person's full name."
        if self.is_staff:
            organizations_ids = Organization.objects.filter(is_active=True).values_list('id', flat=True)
        else:
            organizations_ids = self.organizations.filter(is_active=True).values_list('id', flat=True)
        organizations = Organization.objects.filter(
            Q(id__in=organizations_ids) | Q(owner_id=self.id)
        ).filter(is_active=True)
        return organizations

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


