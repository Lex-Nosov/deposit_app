from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'deposit', views.DepositView, basename='deposit')


urlpatterns = [
    path('', include(router.urls))
]
