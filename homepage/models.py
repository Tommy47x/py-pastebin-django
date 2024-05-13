from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image_url = models.CharField(max_length=2083)


class PasteText(models.Model):
    text = models.CharField(max_length=255)
    
