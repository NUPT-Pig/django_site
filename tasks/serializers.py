from rest_framework import serializers

from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'


class TaskDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'


class MyTaskSerializer(serializers.ModelSerializer):
    manager_names = serializers.SerializerMethodField('get_manager_names')
    executor_names = serializers.SerializerMethodField('get_executor_names')

    class Meta:
        model = Task
        fields = ('id', 'name', 'manager_names', 'executor_names')

    def get_manager_names(self, obj):
        names = []
        for manager in obj.managers.all():
            names.append(manager.user.username)

    def get_executor_names(self, obj):
        executors = []
        for executor in obj.executors.all():
            executors.append(executor.user.username)
