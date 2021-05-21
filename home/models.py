from django.db import models
from datetime import date,datetime
from django.contrib.auth.models import User
# Create your models here.

class Contact(models.Model):


    name = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    phone = models.CharField(max_length=10)
    des = models.TextField()
    date = models.DateField()
    
    def __str__(self): 
        return self.email

class User(models.Model):
    gender=models.CharField(max_length=15)
    date = models.DateField(default="")

class Booking(models.Model):
    order_date = models.DateField()
    user = models.CharField(max_length=25,default="")
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    phone = models.IntegerField()
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=15)
    pincode = models.CharField(max_length=6)
    address = models.TextField()
    des = models.TextField()
    booking_date = models.DateField()
    status = models.BooleanField(default=False)


    def __str__(self):
        
        return self.user
    # current user who book order filter by database
    @staticmethod
    def get_order_by_user(user_id):
        return Booking.objects.filter(user = user_id)

    

class Review(models.Model):
    user = models.CharField(max_length=25,default="")
    review_msg = models.TextField()
    rating = models.CharField(max_length=10)
    date = models.DateField()
    image = models.ImageField(upload_to='reviewimages/')

    def __str__(self):
        
        
        return self.user



    
    
    
