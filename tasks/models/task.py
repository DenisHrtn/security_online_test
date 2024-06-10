from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from .status_choices import TaskStatusChoice

User = get_user_model()


class Task(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tasks_as_customer', verbose_name='Заказчик')
    employee = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='created_tasks_as_employee',
    )
    description = models.TextField(verbose_name="Описание")
    status = models.CharField(
        max_length=20,
        choices=TaskStatusChoice.choices,
        default=TaskStatusChoice.PENDING,
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    closed_at = models.DateTimeField(null=True, blank=True, verbose_name='Дата закрытия')
    report = models.TextField(blank=True, verbose_name='Отчет')

    def save(self, *args, **kwargs):
        if self.pk is not None:
            original = Task.objects.get(pk=self.pk)
            if original.status == 'completed' and (self.status != 'completed' or original.report != self.report):
                raise ValidationError("Выполненную задачу нельзя редактировать.")

        if self.status == 'completed' and not self.report:
            raise ValidationError("Отчет не может быть пустым!")

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Task {self.id} - {self.client.username}"
