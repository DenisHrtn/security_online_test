from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from .base_profile import BaseProfile


class CustomerProfile(BaseProfile):
    age = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(89)],
        verbose_name="Возраст",
    )
    social_network = models.CharField(max_length=125, null=True, blank=True)

    def __str__(self):
        return self.user
