from django.contrib.auth import logout
from django.http import HttpResponse
from rest_framework import permissions
from rest_framework import generics

from security_online_test.swagger_service.auto_schema import apply_swagger_auto_schema
from users.serializers.logout import EmptySerializer


class LogoutView(generics.GenericAPIView):
    """<h2>/api/users/logout/</h2>\n"""

    permission_classes = [permissions.AllowAny]
    serializer_class = EmptySerializer

    def post(self, request):
        logout(request)
        response = HttpResponse(status=200)
        response.delete_cookie("access_token")
        response.delete_cookie("refresh_token")
        return response


LogoutView = apply_swagger_auto_schema(
    tags=["auth"], excluded_methods=[]
)(LogoutView)
