from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', ]
    list_filter = ['is_active', 'is_superuser', ]
    readonly_fields = ['is_active', 'is_superuser', 'user_type', 'password', 'email', 'phone_number', 'last_login']
