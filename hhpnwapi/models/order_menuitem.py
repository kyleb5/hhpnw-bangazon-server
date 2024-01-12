from django.db import models
from .orders import Orders
from .items import Items


class OrderMenuItem(models.Model):
    orders = models.ForeignKey(Orders, on_delete=models.CASCADE)
    items = models.ForeignKey(Items, on_delete=models.CASCADE)
