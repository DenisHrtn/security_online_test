from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework import parsers

from users.models import User
from users.serializers import AssignUserTypeSerializer
from users.permissions import IsEmployeeWithAllTasksPermission
from security_online_test.swagger_service.auto_schema import apply_swagger_auto_schema


class AssignUserTypeView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = AssignUserTypeSerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployeeWithAllTasksPermission]
    parser_classes = (parsers.MultiPartParser, )

    def get_object(self):
        user_id = self.kwargs['pk']
        return generics.get_object_or_404(User, pk=user_id)

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response("Успешно!", status=status.HTTP_200_OK)

    @swagger_auto_schema(auto_schema=None)
    def patch(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def perform_update(self, serializer):
        serializer.save()


AssignUserTypeView = apply_swagger_auto_schema(
    tags=['assign user type'], excluded_methods=[]
)(AssignUserTypeView)
