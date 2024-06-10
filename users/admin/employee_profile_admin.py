from django.contrib import admin

from users.models import EmployeeProfile


@admin.register(EmployeeProfile)
class EmployeeProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'can_view_all_tasks', ]
    readonly_fields = ['user', 'can_view_all_tasks', ]
    list_filter = ['can_view_all_tasks', ]
