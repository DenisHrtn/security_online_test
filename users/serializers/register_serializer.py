from rest_framework import serializers
from django.contrib.auth import get_user_model

from users.models.base_profile import BaseProfile


User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    phone_number = serializers.CharField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)
    password_confirmation = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'phone_number', 'username', 'password', 'password_confirmation')

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirmation']:
            raise serializers.ValidationError("Пароли не совпадают.")

        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError("Пользователь с таким email уже существует.")

        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            password=validated_data['password'],
            username=validated_data.get('username'),  # username передается как ключевой аргумент
        )
        BaseProfile.objects.create(user=user)

        return user
