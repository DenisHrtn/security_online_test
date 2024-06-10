from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema

from tasks.models import Task
from users.permissions import CanAddEmployeeToTask
from security_online_test.swagger_service.auto_schema import apply_swagger_auto_schema


class TaskAssignView(generics.UpdateAPIView):
    queryset = Task.objects.filter(status='pending')
    permission_classes = [IsAuthenticated, CanAddEmployeeToTask]

    def update(self, request, *args, **kwargs):
        task = self.get_object()
        if task.employee:
            return Response(status=status.HTTP_403_FORBIDDEN)
        task.employee = request.user
        task.status = 'in_progress'
        task.save(update_fields=['employee', 'status'])
        return Response("Задача взята в исполнение.", status=status.HTTP_200_OK)

    @swagger_auto_schema(auto_schema=None)
    def patch(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


TaskAssignView = apply_swagger_auto_schema(
    tags=['tasks'], excluded_methods=[]
)(TaskAssignView)
