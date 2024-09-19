import datetime

from rest_framework.test import APITestCase
from .serializers import DepositSerializer
from .models import DepositModel
from datetime import date


class DepositSerializerTest(APITestCase):

    def setUp(self):
        self.url = '127.0.0.1:8000/deposit/'
        self.data = {
            "date": datetime.date.today().strftime('%d.%m.%Y'),
            "periods": 60,
            "amount": 30000,
            "rate": 8.0
        }
        self.data_db = DepositModel.objects.create(**self.data)

    def test_create_db_record(self):
        ser = DepositSerializer(self.data_db)
        self.assertEqual(ser.data, self.data)

    def test_serialization_valid_data(self):
        ser = DepositSerializer(data=self.data)
        self.assertTrue(ser.is_valid())
        self.assertEqual(ser.validated_data, self.data)
