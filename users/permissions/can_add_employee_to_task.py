from rest_framework import permissions

from users.models import UserTypeChoice


class CanAddEmployeeToTask(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        try:
            employee_profile = request.user.baseprofile.employeeprofile
        except AttributeError:
            return False

        if employee_profile.can_view_all_tasks and request.method == "PUT" and not obj.employee:
            return True

        if request.user.user_type == UserTypeChoice.EMPLOYER and not obj.employee:
            return True

        return False
