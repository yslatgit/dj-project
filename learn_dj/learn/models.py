from django.db import models

class LEARN(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table='learn'

class User(models.Model):
    name = models.CharField(max_length=20)
    pwd = models.IntegerField(max_length=20)

    class Meta:
        db_table='user'