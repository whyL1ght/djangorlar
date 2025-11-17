# Django modules
from django.db import models
from django.contrib.auth.models import (
    AbstractUser, 
    AbstractBaseUser, 
    PermissionsMixin,
    BaseUserManager,
)


class CustomUserManager(BaseUserManager):
    """
    Custom user manager
    """
    def obtain_user_instance(
        self, 
        email: str, 
        password: str, 
        **kwargs
        ):
        if not email:
            raise ValueError("Email is required")
        
        new_user: "CustomUser" = self.model(
            email = self.normalize_email(email),
            password = password,
            **kwargs,
        )
        return new_user
    def create_user(
        self, 
        email: str, 
        password: str,
        **kwargs,
        ):
        new_user: "CustomUser" = self.model(
            email = email,
            password = password,
            **kwargs,
        )
        new_user.set_password(password)
        new_user.save(using = self.db)
        return new_user
    
    def create_superuser(
        self,
        email: str,
        password: str,
        **kwargs,
    ):
        new_user: "CustomUser" = self.model(
            email = email,
            password = password,
            is_staff = True,
            is_active = True,
            **kwargs,
        )
        new_user.set_password(password)
        new_user.save(using=self.db)
        return new_user


FIRST_NAME_LENGHT = 100
LAST_NAME_LENGHT = 100
USER_NAME_LENGHT = 200
PHONE_NUMBER_LENGHT = 20
CITY_NAME_LENGHT = 100
COUNTRY_NAME_LENGHT = 100
DEPARTMENTS_NAME_LENGHT = 50
ROLE_NAME_LENGHT = 20

class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    CustomUser class created by AbstractBase user and PermissionsMixin
    """
    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("manager", "Manager"),
        ("employee", "Employee"),
    )
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=200, unique=True)
    first_name = models.CharField(max_length=FIRST_NAME_LENGHT)
    last_name = models.CharField(max_length=LAST_NAME_LENGHT)
    phone = models.CharField(max_length=PHONE_NUMBER_LENGHT)
    city = models.CharField(max_length=CITY_NAME_LENGHT, blank=True)
    country = models.CharField(max_length=COUNTRY_NAME_LENGHT, blank=True)
    department = models.CharField(max_length=DEPARTMENTS_NAME_LENGHT)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    birth_date = models.DateField(null=True, blank=True)
    salary = models.IntegerField(null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email

