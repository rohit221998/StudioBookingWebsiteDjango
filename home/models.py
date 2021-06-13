from django.db import models
from datetime import datetime,date
from django.contrib.auth.models import User
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    phone = models.CharField(max_length=10)
    des = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

 



class Booking(models.Model):
    order_date = models.DateField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    phone = models.IntegerField()
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=15)
    pincode = models.CharField(max_length=6)
    address = models.TextField()
    des = models.TextField()
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    

class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)   
    review_msg = models.TextField()
    rating = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='reviewimages/')

   



    
    
    
