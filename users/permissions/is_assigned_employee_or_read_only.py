from rest_framework import permissions


class IsAssignedEmployeeOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.employee:
            return True
        return False
