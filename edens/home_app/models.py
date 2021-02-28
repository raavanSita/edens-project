from typing import ClassVar
from django.db import models

# Create your models here.
class slideHead (models.Model):
    title = models.CharField(max_length=250)
    subTitle = models.CharField(max_length=250)
    image = models.ImageField()

    def __str__(self):  
        return self.title
class inner (models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField()
    color = models.CharField(max_length=250,default='#FFFF')
    def __str__(self):  
        return self.title

class catogeryTitle (models.Model):
    title = models.CharField(max_length=10)
    def __str__(self):  
        return self.title
class arrivalsContent (models.Model):
    title = models.CharField(max_length=30)

    price = models.FloatField()

    image = models.ImageField()

    sortType = models.CharField(max_length=20,default="*")

class hotsale(models.Model):
    image = models.ImageField()
    headline = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    original_price = models.FloatField()
    offer_price = models.FloatField()

class MENS_catogery (models.Model):
    title = models.CharField(max_length=30)

    price = models.FloatField()

    image = models.ImageField()

    sortType = models.CharField(max_length=20,default="*")

class WOMENS_catogery (models.Model):
    title = models.CharField(max_length=30)

    price = models.FloatField()

    image = models.ImageField()

    sortType = models.CharField(max_length=20,default="*")

class KIDS_catogery (models.Model):
    title = models.CharField(max_length=30)

    price = models.FloatField()

    image = models.ImageField()

    sortType = models.CharField(max_length=20,default="*")

class FOOTWEAR_catogery (models.Model):
    title = models.CharField(max_length=30)

    price = models.FloatField()

    image = models.ImageField()

    sortType = models.CharField(max_length=20,default="*")