from django.contrib.auth.models import User
from students.models import Students
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class StudentsSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField("get_user_name")

    class Meta:
        model = Students
        fields = '__all__'

    def get_user_name(self, obj):
        username = ""
        try:
            username = obj.user.username
        except Exception as e:
            print str(e)
        return username