from django.db import models


class SexChoices(models.TextChoices):
    MAN = "Мужской"
    WOMAN = "Женский"
    NO_SELECTED = "Не выбрано"
