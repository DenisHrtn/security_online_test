from rest_framework import permissions


class IsTaskOwnerOrAssignedEmployeeOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.customer or request.user == obj.employee:
            return True
        try:
            return request.user.baseprofile.employeeprofile.can_view_all_tasks
        except AttributeError:
            return False
