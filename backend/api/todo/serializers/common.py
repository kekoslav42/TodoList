from rest_framework import serializers

from apps.todo.models import TodoRecord


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoRecord
        fields = ("uuid", "body", "created", "active")
