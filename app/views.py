from .models import DepositModel
from .serializers import DepositSerializer
from .service import deposit_calculation

from rest_framework import response
from rest_framework import viewsets
from rest_framework import status


class DepositView(viewsets.ModelViewSet):
    serializer_class = DepositSerializer
    queryset = DepositModel.objects.all()

    def create(self, request, *args, **kwargs) -> response.Response:
        data = request.data
        ser = DepositSerializer(data=data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            deposit_calculation_result = deposit_calculation(date=data['date'], periods=data['periods'],
                                                             amount=data['amount'], rate=data['rate'])
            return response.Response(data=deposit_calculation_result, status=status.HTTP_200_OK)
        else:
            return response.Response(data={"error": ser.error_messages}, status=status.HTTP_400_BAD_REQUEST)
