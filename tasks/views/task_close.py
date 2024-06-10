from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser

from tasks.models import Task
from tasks.serializers import TaskCloseSerializer
from users.permissions import IsAssignedEmployeeOrReadOnly
from security_online_test.swagger_service.auto_schema import apply_swagger_auto_schema


class TaskCloseView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCloseSerializer
    permission_classes = [permissions.IsAuthenticated, IsAssignedEmployeeOrReadOnly]
    parser_classes = [MultiPartParser, ]

    def update(self, request, *args, **kwargs):
        task = self.get_object()
        if task.status != 'in_progress':
            return Response({"detail": "Task is not in progress."}, status=status.HTTP_400_BAD_REQUEST)
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(auto_schema=None)
    def patch(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


TaskCloseView = apply_swagger_auto_schema(
    tags=['tasks'], excluded_methods=[]
)(TaskCloseView)
