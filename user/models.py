import django
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, PermissionsMixin
from django.db import models


PACKAGE_BASIC = 10
PACKAGE_FOOD = 20
PACKAGE_SHIRT = 30
PACKAGE_SHIRT_FOOD = 40


PACKAGE_CHOICES = [
    (PACKAGE_BASIC, "Basic Package (No food, No shirt)"),
    (PACKAGE_FOOD, "Basic Package + food (No shirt)"),
    (PACKAGE_SHIRT, "Basic Package + shirt (No food)"),
    (PACKAGE_SHIRT_FOOD, "Total Package (Food + Shirt)")
]


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=40, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(('first name'), max_length=64, default='', blank=True)
    last_name = models.CharField(('last name'), max_length=150, default='', blank=True)
    date_joined = models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')
    package = models.PositiveSmallIntegerField(choices=PACKAGE_CHOICES, default=PACKAGE_BASIC, db_index=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.username
