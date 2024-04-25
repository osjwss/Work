from django.db import models

# Create your models here.

class Car(models.Model):
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.IntegerField(null=True, blank=True)
    manufacturer = models.ForeignKey('Manufacturer',on_delete=models.CASCADE)

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    counrty = models.CharField(max_length=100)
