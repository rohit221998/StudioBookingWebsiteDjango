from django.contrib import admin
from home.models import Contact
from home.models import Booking
from home.models import Review
# Register your models here.

# admin.site.register(Contact)
# admin.site.register(Booking)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=['email', 'name', 'date', 'phone']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display=['user_id','user' ,'email','order_date', 'booking_date']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display=['user_id','user','rating','date']
