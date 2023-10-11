from django.db import models


class Results(models.Model):
    area = models.IntegerField()
    price = models.IntegerField()
# Create your models here.
