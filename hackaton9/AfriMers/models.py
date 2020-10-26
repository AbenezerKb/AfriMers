from django.db import models

# Create your models here.
class Farmer(models.Model):
    fullName = models.CharField(max_length=60)
    email = models.CharField(max_length=40)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    phone = models.BigIntegerField
    password = models.CharField(max_length=10)
    date_created = models.DateTimeField(auto_now_add=True)

class Grocery(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.CharField(max_length=20)
    size = models.IntegerField
    price = models.IntegerField
    itemimage = models.FileField(max_length=250)
    email = models.ForeignKey(Farmer, on_delete=models.CASCADE)

class Purchaser(models.Model):
    fullName = models.CharField(max_length=60)
    email = models.CharField(max_length=40)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    phone = models.BigIntegerField
    password = models.CharField(max_length=10)
    date_created = models.DateTimeField(auto_now_add=True)

class SoldItems(models.Model):
    id = models.AutoField(primary_key=True)
    farm_email = models.CharField(max_length=40)
    purch_email = models.CharField(max_length=40)
    amount = models.IntegerField
    price = models.IntegerField
    date_created = models.DateTimeField(auto_now_add=True)
