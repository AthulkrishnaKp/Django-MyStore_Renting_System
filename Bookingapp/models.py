from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Products(models.Model):
    name=models.CharField(max_length=200)
    price_for_a_day=models.PositiveIntegerField()
    CATEGORY = (
        ('books', 'Books'),
        ('clothings', 'Clothings'),
        ('electronics', 'Electronics'),
    )
    category=models.CharField(choices=CATEGORY,max_length=200,default=3)
    qty=models.PositiveIntegerField(default=1)
    seller=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Booking(models.Model):
    customer_name=models.CharField(max_length=200)
    customer_num=models.IntegerField()  
    customer_address=models.CharField(max_length=400)
    item=models.ForeignKey(Products,on_delete=models.CASCADE)
    rent_date=models.DateField()
    return_date=models.DateField()
