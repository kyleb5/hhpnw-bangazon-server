from django.db import models


class Orders(models.Model):

    customerEmail = models.EmailField()
    customerPhone = models.IntegerField()
    date = models.IntegerField()
    open = models.BooleanField()
    orderName = models.CharField(max_length=12)
    orderType = models.CharField(max_length=12)
    uid = models.TextField(max_length=50)
