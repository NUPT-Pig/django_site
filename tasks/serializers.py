from rest_framework import serializers

from tasks.models import Task


class TaskListSerializer(serializers.ModelSerializer):
    manager_names = serializers.SerializerMethodField()
    executor_names = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ('id', 'name', 'manager_names', 'executor_names', 'finish_time', 'level')

    def get_manager_names(self, obj):
        names = []
        for manager in obj.managers.all():
            names.append(manager.user.username)
        return names

    def get_executor_names(self, obj):
        names = []
        for manager in obj.executors.all():
            names.append(manager.user.username)
        return names


class TaskCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'


class TaskDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'

