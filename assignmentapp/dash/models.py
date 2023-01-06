

from django.db.models.deletion import CASCADE, SET_DEFAULT, SET_NULL
from django.core import serializers
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Products(models.Model):
 productchoices = (
    ('Goods','Goods'),
    ('Electronics','Electronics'),
    ('Foods','Foods'),
    ('Bags','Bags'),
 )
 title = models.CharField(max_length=50)
 description = models.CharField(max_length=300,blank=True, default='')
 price = models.IntegerField()
 quantity = models.IntegerField()
 productimage = models.ImageField(upload_to="media",blank=True, default='media/bag_6fTAjkq.jpg')
 productcategory = models.CharField(max_length=15, choices=productchoices, blank=True)

 