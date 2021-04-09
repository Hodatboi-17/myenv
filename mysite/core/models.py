from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.FloatField(default=0)

