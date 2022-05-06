from rest_framework import serializers

from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    description = serializers.CharField(required=False)

    class Meta:
        model = Task
        fields = ('id', 'title', 'complete', 'created', 'description')
