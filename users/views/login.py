from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import AllowAny
from rest_framework import generics

from users.serializers.login_serializer import LoginSerializer
from security_online_test.swagger_service.auto_schema import apply_swagger_auto_schema


class LoginView(generics.GenericAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = LoginSerializer
    parser_classes = (MultiPartParser,)

    def post(self, request):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']

        if user:
            access_token = AccessToken.for_user(user)
            refresh_token = RefreshToken.for_user(user)
            response = Response({'message': 'Logged in successfully'})
            response.set_cookie(key='access_token', value=access_token, httponly=True)
            response.set_cookie(key='refresh_token', value=refresh_token, httponly=True)
            return response
        else:
            response = Response({'message': "Что-то пошло не так!"})

            return response


LoginView = apply_swagger_auto_schema(
    tags=["auth"], excluded_methods=[]
)(LoginView)
