from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action

from users.models.user import User, UserTypeChoice
from users.serializers.users_serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    <h2>
    Эндпоинт отдает всех пользователей, кроме заказчиков, если запрос делает сотрудник. Заказчик и супер пользователь
    видят всех кроме себя. Эндпоинт me отдает пользователя сделавшего запрос.
    </h2>
    """
    permission_classes = [IsAuthenticated, ]
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.exclude(is_superuser=True)
        if self.request.user.user_type == UserTypeChoice.CUSTOMER:
            return User.objects.exclude(is_superuser=True, is_staff=True, id=self.request.user.id)
        if self.request.user.user_type == UserTypeChoice.EMPLOYER:
            return User.objects.exclude(is_superuser=True, is_staff=True, user_type=UserTypeChoice.EMPLOYER)
        return User.objects.none()

    @action(detail=False, methods=['GET'])
    def me(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    @swagger_auto_schema(auto_schema=None)
    def create(self, request, *args, **kwargs):
        return Response("Method Not Allowed", status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @swagger_auto_schema(auto_schema=None)
    def update(self, request, *args, **kwargs):
        return Response("Method Not Allowed", status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @swagger_auto_schema(auto_schema=None)
    def destroy(self, request, *args, **kwargs):
        return Response("Method Not Allowed", status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @swagger_auto_schema(auto_schema=None)
    def partial_update(self, request, *args, **kwargs):
        return Response("Method Not Allowed", status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @swagger_auto_schema(auto_schema=None)
    def retrieve(self, request, *args, **kwargs):
        return Response("Method Not Allowed", status=status.HTTP_405_METHOD_NOT_ALLOWED)
