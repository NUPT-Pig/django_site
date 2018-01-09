from rest_framework import serializers

from tasks.models import Task


class TaskListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'name', 'finish_time', 'level')


class TaskCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'


class TaskDetailSerializer(serializers.ModelSerializer):
    manager_names = serializers.SerializerMethodField()
    executor_names = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = '__all__'

    def get_manager_names(self, obj):
        names = []
        for manager in obj.managers.all():
            names.append({'name': manager.user.username, 'id': manager.id})
        return names

    def get_executor_names(self, obj):
        names = []
        for executor in obj.executors.all():
            names.append({'name': executor.user.username, 'id': executor.id})
        return names


