from rest_framework import permissions


class IsEmployeeWithAllTasksPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            employee_profile = request.user.baseprofile.employeeprofile
            return employee_profile.can_view_all_tasks
        except AttributeError:
            return False
