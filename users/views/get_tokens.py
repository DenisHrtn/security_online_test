from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from security_online_test.swagger_service.auto_schema import apply_swagger_auto_schema


class CurrentUserTokensView(APIView):
    """
    <h2>
    Эндпоинт для получения токенов
    Отдает ID пользователя и его токены.
    </h2>
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        access_token = str(request.auth)
        refresh_token = str(request.COOKIES.get('refresh_token'))

        return Response({
            'user_id': user.id,
            'access_token': access_token,
            'refresh_token': refresh_token,
        }, status=status.HTTP_200_OK)


CurrentUserTokensView = apply_swagger_auto_schema(
    tags=['tokens'], excluded_methods=[]
)(CurrentUserTokensView)
