from rest_framework import serializers
from .models import DepositModel


class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositModel
        fields = '__all__'
