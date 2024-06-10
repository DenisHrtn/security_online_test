from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser
from django.contrib.auth import get_user_model
from rest_framework import generics

from users.serializers.register_serializer import RegisterSerializer
from security_online_test.swagger_service.auto_schema import apply_swagger_auto_schema

User = get_user_model()


class RegisterAPI(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    parser_classes = (MultiPartParser, )

    def post(self, request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response("Пользователь успешно зарегистрирован.", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


RegisterAPI = apply_swagger_auto_schema(
    tags=['auth'], excluded_methods=[]
)(RegisterAPI)
