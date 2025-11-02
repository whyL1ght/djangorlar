# Django modules
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin

PHONE_NUMBER_LENGHT = 20

class CustomUser(AbstractUser):
    """
    CustomUser class created by AbstractUser
    """
    phone_number = models.CharField(max_length=PHONE_NUMBER_LENGHT)

FIRST_NAME_LENGHT = 100
LAST_NAME_LENGHT = 100
USER_NAME_LENGHT = 200

class CustomUser2(AbstractBaseUser, PermissionsMixin):
    """
    CustomUser class created by AbstractBase user and PermissionsMixin
    """
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=200, unique=True)
    first_name = models.CharField(max_length=FIRST_NAME_LENGHT)
    last_name = models.CharField(max_length=LAST_NAME_LENGHT)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username

