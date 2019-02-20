from django.db import models


class Location(models.Model):
    timestamp = models.IntegerField()
    lat = models.FloatField()
    lon = models.FloatField()
