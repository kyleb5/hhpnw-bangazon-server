from django.db import models


class User(models.Model):
    uid = models.TextField()
    joinDate = models.IntegerField()
    hasAccess = models.BooleanField()  # Access has to be manually given from an Admin
