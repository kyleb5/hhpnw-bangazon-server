from django.db import models


class Orders(models.Model):

    customerEmail = models.EmailField()
    customerPhone = models.IntegerField()
    date = models.DateField()
    open = models.BooleanField()
    orderName = models.CharField(max_length=12)
    orderType = models.CharField(max_length=12)
    uid = models.CharField(max_length=50)
