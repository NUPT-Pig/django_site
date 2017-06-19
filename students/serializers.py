from django.contrib.auth.models import User
from students.models import Student
from rest_framework import serializers
from common_interface.log_interface import get_logger
logger = get_logger()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField("get_user_name")

    class Meta:
        model = Student
        fields = '__all__'

    def get_user_name(self, obj):
        username = ""
        try:
            username = obj.user.username
        except Exception as e:
            logger.error(str(e))
        return username