from django.db import models


class FinalRes(models.Model):
    battery_power = models.IntegerField()
    int_memory = models.IntegerField()
    mobile_wt = models.IntegerField()
    category = models.IntegerField()
# Create your models here.
