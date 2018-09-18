from django.db import models

# Create your models here.

class User(models.Model):
    Name = models.CharField(max_length=200)
    Created = models.DateTimeField('date created')
    Updated = models.DateTimeField('date updated')

class Product(models.Model):
    Name = models.CharField(max_length=200)
    Price = models.CharField(max_length=200)
    Quantity = models.IntegerField(default=0)
    Created = models.DateTimeField('date created')
    Updated = models.DateTimeField('date updated')

class Order(models.Model):
    Billing_Address = models.CharField(max_length=200)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
