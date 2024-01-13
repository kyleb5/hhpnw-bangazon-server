from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    uid = models.CharField(max_length=30)
    joinDate = models.IntegerField()
    hasAccess = models.BooleanField()  # Access has to be manually given from an Admin
