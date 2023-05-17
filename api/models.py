from django.db import models

# Create your models here.
class Point(models.Model):
    id=models.IntegerField(primary_key=True)
    points = models.CharField(max_length=200)
    close_points= models.CharField(max_length=200)
