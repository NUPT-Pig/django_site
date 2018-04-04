from rest_framework import serializers
from django.conf import settings

from helper.models import Account, User

from common_interface.log_interface import get_logger
logger = get_logger()


class AccountSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = ['id', 'username', 'money', 'date', 'valid']

    def get_username(self, obj):
        return obj.user.username


class AccountDetailSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = '__all__'

    def get_username(self, obj):
        return obj.user.username