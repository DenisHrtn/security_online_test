from rest_framework import generics
from rest_framework import permissions

from tasks.models import Task
from tasks.serializers import TaskSerializer
from security_online_test.swagger_service.auto_schema import apply_swagger_auto_schema


class MyTasksAPI(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'baseprofile') and hasattr(user.baseprofile, 'employeeprofile'):
            return Task.objects.filter(employee=user)
        return Task.objects.none()


MyTasksAPI = apply_swagger_auto_schema(
    tags=['tasks'], excluded_methods=[]
)(MyTasksAPI)
