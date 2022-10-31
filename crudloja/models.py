from django.db import models

class Produto(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    quantityStock = models.IntegerField()
    

# Create your models here.
