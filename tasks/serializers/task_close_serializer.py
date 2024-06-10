from rest_framework import serializers
from django.utils import timezone

from tasks.models import Task


class TaskCloseSerializer(serializers.ModelSerializer):
    report = serializers.CharField()

    class Meta:
        model = Task
        fields = ['report']

    def update(self, instance, validated_data):
        instance.report = validated_data.get('report', instance.report)
        instance.status = 'done'
        instance.closed_at = timezone.now()
        instance.save()
        return instance
