from rest_framework import permissions

from users.models import UserTypeChoice


class CanViewAllTasks(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            employee_profile = request.user.baseprofile.employeeprofile
        except AttributeError:
            employee_profile = None

        if employee_profile and (employee_profile.can_view_all_tasks or request.user.user_type == UserTypeChoice.EMPLOYER):
            return True

        if request.user.user_type == UserTypeChoice.CUSTOMER:
            return request.method in permissions.SAFE_METHODS

        return False

    def has_object_permission(self, request, view, obj):
        if not obj.employee or obj.employee == request.user:
            return True
        return False
