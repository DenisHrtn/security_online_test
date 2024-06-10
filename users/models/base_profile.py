from django.db import models

from .sex_choice import SexChoices


class BaseProfile(models.Model):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE, primary_key=True)
    sex = models.CharField(max_length=20, choices=SexChoices.choices, default=SexChoices.NO_SELECTED)
    country = models.CharField(max_length=125, default="Не указано", blank=False)
    city = models.CharField(max_length=125, default="Не указано", blank=False)
