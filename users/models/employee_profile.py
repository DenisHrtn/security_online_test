from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from .base_profile import BaseProfile


class EmployeeProfile(BaseProfile):
    age = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(89)],
        verbose_name="Возраст",
    )
    telegram = models.CharField(max_length=125, null=True, blank=True)
    experience = models.CharField(max_length=125, null=True, blank=True)
    can_view_all_tasks = models.BooleanField(default=False)

    def __str__(self):
        return self.user
