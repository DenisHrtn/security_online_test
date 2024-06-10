from django.contrib import admin

from tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['customer', 'employee', 'status', ]
    list_filter = ['customer', 'employee', 'status', ]
    readonly_fields = ['customer', 'employee', 'status', ]
