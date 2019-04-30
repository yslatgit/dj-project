from django.db import models
from django.contrib.auth.models import AbstractUser
class LEARN(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table='learn'

class User(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=20,default='a')
    pwd = models.CharField(max_length=100)

    class Meta:
        db_table='user'

class City(models.Model):
    """城市关系类"""
    cname = models.CharField(max_length=20)
    depart = models.IntegerField(max_length=11)

    class Meta:
        db_table='city'