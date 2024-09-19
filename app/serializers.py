from rest_framework import serializers
from .models import DepositModel


class DepositSerializer(serializers.ModelSerializer):
    date = serializers.DateField(read_only=False)

    class Meta:
        model = DepositModel
        fields = ['date', 'periods', 'amount', 'rate']
