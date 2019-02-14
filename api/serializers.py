from rest_framework import serializers
from core.models import User, List, Task


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = (
            'name',
            'time_allocated',
            'time_remaining',
            'list',
            'category',
            'pk',
            'completed',
        )


class ListSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(read_only=True, many=True)

    class Meta:
        model = List
        fields = (
            'title',
            'date',
            'user',
            'pk',
            'completed',
            'tasks',
        )


class UserSerializer(serializers.ModelSerializer):
    lists = ListSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = (
            'username',
            'lists',
            'pk',
        )
