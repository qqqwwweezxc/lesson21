from rest_framework import serializers
from django.utils import timezone
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email"]


class TasksSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=100)
    due_date = serializers.DateField()
    user = UserSerializer()

    def validate_due_date(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError(
                "Date cannot be in the past"
            )

        return value