from rest_framework import serializers

from teachers.models import Teacher

from common_interface.log_interface import get_logger
logger = get_logger()


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = '__all__'


class TeacherDetailSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField("get_user_name")

    class Meta:
        model = Teacher
        fields = '__all__'

    def get_user_name(self, obj):
        username = ""
        try:
            if obj.user:
                username = obj.user.username
        except Exception as e:
            logger.error(str(e))
        return username
