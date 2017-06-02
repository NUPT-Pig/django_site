from django.contrib.auth.models import User
from students.models import Students
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'