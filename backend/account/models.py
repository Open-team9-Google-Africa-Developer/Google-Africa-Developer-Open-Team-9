from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token
from .manager import CustomUserManager
# Create your models here.

class CustomUser(AbstractUser):

    """ 
    Custom User Model that Uses email as a unique username
    """
    is_admin = models.BooleanField(default=False)

    username = None
    email = models.EmailField(("email address"), unique=True)
    phone_number = PhoneNumberField(max_length=15, unique=True, null=True, default=None)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    @property
    def get_full_name(self):
        return super().get_full_name()

    def __str__(self):
        if self.first_name:
            return self.first_name
        return self.email


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
