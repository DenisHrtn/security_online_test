from rest_framework import serializers

from users.models import User, UserTypeChoice, EmployeeProfile, CustomerProfile


class AssignUserTypeSerializer(serializers.ModelSerializer):
    user_type = serializers.ChoiceField(choices=UserTypeChoice.choices)

    class Meta:
        model = User
        fields = ['user_type']

    def validate(self, data):
        user = self.instance
        if user.user_type:
            raise serializers.ValidationError("Тип пользователя уже записан и не может быть переназначен.")
        return data

    def update(self, instance, validated_data):
        instance.user_type = validated_data['user_type']
        if validated_data['user_type'] == 'employer':
            EmployeeProfile.objects.create(user=instance, age=0)
        if validated_data['user_type'] == 'customer':
            CustomerProfile.objects.create(user=instance, age=0)
        instance.save(update_fields=['user_type'])
        return instance
