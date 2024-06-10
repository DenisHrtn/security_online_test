from django.db import models


class TaskStatusChoice(models.TextChoices):
    PENDING = 'pending', 'Ожидает исполнителя'
    IN_PROGRESS = 'in_progress', 'В процессе'
    DONE = 'done', 'Выполнена'
