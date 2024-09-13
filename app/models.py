from django.db import models
from django.core import validators


class DepositModel(models.Model):
    date = models.DateField()
    periods = models.IntegerField(validators=[validators.MinValueValidator(1),
                                              validators.MaxValueValidator(60)])
    amount = models.IntegerField(validators=[validators.MinValueValidator(10_000),
                                             validators.MaxValueValidator(3_000_000)])
    rate = models.FloatField(validators=[validators.MinValueValidator(1),
                                         validators.MaxValueValidator(8)])
