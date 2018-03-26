from rest_framework import serializers

from helper.models import Account

from common_interface.log_interface import get_logger
logger = get_logger()

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
