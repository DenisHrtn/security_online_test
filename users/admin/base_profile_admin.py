from django.contrib import admin

from users.models import BaseProfile


@admin.register(BaseProfile)
class BaseProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'sex', ]
    list_filter = ['user', 'sex', ]
    search_fields = ['user', ]
    readonly_fields = ['user', ]
