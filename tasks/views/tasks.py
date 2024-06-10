from django.db.models import Q
from rest_framework import generics, status, serializers
from rest_framework.parsers import MultiPartParser
from rest_framework import permissions
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from tasks.models.task import Task
from tasks.serializers.tasks_serializer import TaskSerializer
from users.models import UserTypeChoice, User
from users.permissions import CanViewAllTasks, IsAssignedEmployeeOrReadOnly, IsTaskOwnerOrAssignedEmployeeOrReadOnly
from security_online_test.swagger_service.auto_schema import apply_swagger_auto_schema


class TaskListCreateView(generics.ListCreateAPIView):
    """
    <h2>
    Просматривать все таски может любой, но если таска взята в исполнение, то она исчезнет из общего списка. Заказчик
    видит только свои таски, сотрудник со всеми правами - все. Создавать таски может сотрудник со всеми правами и
    заказчик. При создании таски заказчиком ему не нужно указывать свое ID.
    </h2>
    """

    serializer_class = TaskSerializer
    parser_classes = (MultiPartParser,)

    def get_queryset(self):
        user = self.request.user
        if user.user_type == UserTypeChoice.CUSTOMER:
            return Task.objects.filter(customer=user)
        if hasattr(user, 'baseprofile') and hasattr(user.baseprofile, 'employeeprofile'):
            employee_profile = user.baseprofile.employeeprofile
            if employee_profile.can_view_all_tasks:
                return Task.objects.all()
            else:
                return Task.objects.filter(Q(employee=user) | Q(employee=None))
        return Task.objects.none()

    def get_permissions(self):
        if self.request.method == 'POST':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAuthenticated, CanViewAllTasks]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        user = self.request.user
        if user.user_type == UserTypeChoice.CUSTOMER:
            serializer.save(customer=user)
        elif hasattr(user, 'baseprofile') and hasattr(user.baseprofile, 'employeeprofile'):
            employee_profile = user.baseprofile.employeeprofile
            if employee_profile.can_view_all_tasks:
                customer_id = self.request.data.get('customer')
                if customer_id:
                    customer_instance = User.objects.get(pk=customer_id)
                    serializer.save(customer=customer_instance)
                else:
                    raise serializers.ValidationError("Заказчик должен быть указан.")
            else:
                raise serializers.ValidationError("У Вас нету прав для создания задач заказчикам.")
        else:
            raise serializers.ValidationError("Неправильный тип пользователя.")


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    <h2>
    Изменять таску может только сотрудник со всеми правами. Он может переназначить заказчика и поменять описание.
    Методы PATCH и DELETE запрещены.
    </h2>
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    parser_classes = (MultiPartParser,)

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH']:
            permission_classes = [permissions.IsAuthenticated, IsTaskOwnerOrAssignedEmployeeOrReadOnly]
        else:
            permission_classes = [permissions.IsAuthenticated, IsAssignedEmployeeOrReadOnly]
        return [permission() for permission in permission_classes]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        if instance.status != 'pending':
            return Response(
                {"detail": "Задачу нельзя обновлять, если статус не pending"},
                status=status.HTTP_400_BAD_REQUEST
            )

        data = request.data.copy()
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @swagger_auto_schema(auto_schema=None)
    def patch(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @swagger_auto_schema(auto_schema=None)
    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


TaskListCreateView = apply_swagger_auto_schema(
    tags=['tasks'], excluded_methods=[]
)(TaskListCreateView)

TaskDetailView = apply_swagger_auto_schema(
    tags=['tasks'], excluded_methods=[]
)(TaskDetailView)
