from django.contrib.auth.hashers import check_password
from django.db.models import Q
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', ]

    def validate(self, attrs):
        password = attrs.get("password")
        user = User.objects.filter(Q(email=attrs.get('email'))).first()
        if not user:
            raise serializers.ValidationError("Неправильные учетные данные.")

        if not check_password(password, user.password):
            raise serializers.ValidationError("Неправильный пароль.")

        attrs["user"] = user
        return attrs
