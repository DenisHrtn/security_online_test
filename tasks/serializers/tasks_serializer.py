from rest_framework import serializers

from tasks.models.task import Task
from users.models import User, UserTypeChoice


class TaskSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.filter(user_type=UserTypeChoice.CUSTOMER), required=False
    )

    class Meta:
        model = Task
        fields = ['id', 'customer', 'employee', 'created_at', 'updated_at', 'closed_at', 'report', 'status', 'description']
        read_only_fields = ['employee', 'updated_at', 'closed_at', 'report', 'status']

    def validate(self, data):
        request = self.context.get('request')
        if request.user.user_type != UserTypeChoice.CUSTOMER:
            if 'customer' not in data:
                raise serializers.ValidationError("Поле 'Клиент' обязательное.")
        return data

    def create(self, validated_data):
        customer = validated_data.get('customer')
        if isinstance(customer, int):
            customer = User.objects.get(pk=customer)
            validated_data['customer'] = customer
        return Task.objects.create(**validated_data)
