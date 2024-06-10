from django.contrib import admin

from users.models import CustomerProfile


@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ['user', ]
    search_fields = ['user', ]
    list_filter = ['user', ]
