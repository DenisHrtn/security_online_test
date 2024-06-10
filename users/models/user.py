from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser

from .user_type import UserTypeChoice
from users.managers.user_manager import UserManager


class User(AbstractUser):
    id = models.AutoField(primary_key=True, editable=False, verbose_name="ID пользователя")
    email = models.EmailField(unique=True, verbose_name="email пользователя")
    username = models.CharField(
        null=True,
        blank=True,
        max_length=25,
        verbose_name="username пользователя",
    )
    phone_number = PhoneNumberField(null=True, blank=True, verbose_name="Номер телефона")
    user_type = models.CharField(max_length=20, choices=UserTypeChoice.choices, default='')
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']

    def __str__(self):
        return self.email
