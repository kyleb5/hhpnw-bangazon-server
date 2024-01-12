from django.db import models
from .orders import Orders


class Revenue(models.Model):
    date = models.IntegerField()
    orderid = models.ForeignKey(Orders, on_delete=models.CASCADE)
    tipAmount = models.DecimalField(max_digits=10, decimal_places=2)
    paymentType = models.CharField(max_length=12)
