from django.db import models


class UserTypeChoice(models.TextChoices):
    EMPLOYER = 'employer', 'Employer'
    CUSTOMER = 'customer', 'Customer'
