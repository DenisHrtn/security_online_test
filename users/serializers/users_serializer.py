from rest_framework import serializers

from users.models.user import User
from users.models.base_profile import BaseProfile
from users.models.customer_profile import CustomerProfile
from users.models.employee_profile import EmployeeProfile
from users.serializers.employee_profile_serializer import EmployeeProfileSerializer
from users.serializers.customer_profile_serializer import CustomerProfileSerializer
from users.models.user_type import UserTypeChoice


class UserSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'phone_number',
            'username',
            'user_type',
            'date_joined',
            'profile'
        ]

    def get_profile(self, obj):
        base_profile = BaseProfile.objects.filter(user=obj).first()

        if not base_profile:
            return None

        serializer = None

        if obj.user_type == UserTypeChoice.EMPLOYER:
            profile = EmployeeProfile.objects.filter(baseprofile_ptr_id=base_profile.pk).first()
            if profile:
                serializer = EmployeeProfileSerializer(profile)
        if obj.user_type == UserTypeChoice.CUSTOMER:
            profile = CustomerProfile.objects.filter(baseprofile_ptr_id=base_profile.pk).first()
            if profile:
                serializer = CustomerProfileSerializer(profile)

        return serializer.data if serializer else None
