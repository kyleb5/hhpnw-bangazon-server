from django.db import models


class Items(models.Model):
    name = models.CharField(max_length=12)
    img = models.CharField(max_length=255)
    price = models.IntegerField()
    type = models.CharField(max_length=20)
    description = models.TextField()
