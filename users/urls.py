from rest_framework import routers
from django.urls import path

from users.views.register import RegisterAPI
from users.views.login import LoginView
from users.views.logout import LogoutView
from users.views.users import UserViewSet
from users.views.get_tokens import CurrentUserTokensView
from users.views.assign_user_type import AssignUserTypeView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')


urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('tokens/', CurrentUserTokensView.as_view(), name='tokens'),
    path('assign-user-type/<int:pk>/', AssignUserTypeView.as_view(), name='assign-user-type'),
] + router.urls
