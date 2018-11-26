from django.db import models

# Create your models here.

class Stats(models.Model):
  name = models.CharField(max_length=100)
  rank = models.IntegerField()
  leader = models.CharField(max_length=100)
  stat1 = models.IntegerField()
  stat2 = models.IntegerField()