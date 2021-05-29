from django.shortcuts import render , HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from home.models import Booking
from home.models import Review
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import logout, login
from .models import Booking
# from app.forms import ModificationForm
from django.contrib.auth.decorators import login_required



# Create views here manualy.

def index(request):
  

  context = {
       "variable1":"Singh is great",
       "variable2":"this is about"
      }    
  return render(request,'index.html',context)
    
  #  return HttpResponse("this is homepage")

def about(request):

    #return HttpResponse("this is about page") 
     return render(request,'about.html')

def contact(request):
  if request.method == "POST":
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    des = request.POST.get('des')
    contact = Contact(name=name, email=email, phone=phone,des=des, date=datetime.today())
    contact.save()
    messages.success(request,'Your message has been sent!!!')
  return render(request,'contact.html')
    #return HttpResponse("this is contactpage") 

def services(request):
  if request.user.is_anonymous:
     return redirect("/sign")
  return render(request,'services.html')

def sign(request):
  
  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username, password)

    #check user has correct credentails
    user = authenticate(username=username, password=password)

    if user is not None:
      # A backend authenticated the credentials
      login(request, user)

      # Session : which user login in session time
      request.session['user'] = username
      messages.success(request,'Successful login!!!')
      return redirect("/")

    else:
      # No backend authenticated the credentials
      messages.success(request,'inavali input!!!')
      return render(request,'sign.html')
    

  return render(request,'sign.html')

@login_required

def signout(request):
  logout(request)
  return redirect("/sign")

def registration(request): 
  if request.method =="POST":
    username = request.POST.get('username')
    password = request.POST.get('password')
    firstname = request.POST.get('firstname')
    lastname = request.POST.get('lastname')
    email = request.POST.get('email')
   
    #create user and save data
    myuser = User.objects.create_user(username,email,password)
    myuser.first_name = firstname
    myuser.last_name = lastname
    myuser.save()
    messages.success(request,'Your Account Successful Created..pls login!!!')
   
  return render(request,'registration.html')
  # else:
  #   return HttpResponse('404 - Not Found')

@login_required
def profile(request):
  args = {'user':request.user}
  
  return render(request,'profile.html',args)  

@login_required
def myorder(request):
  user = request.session.get('user')
  bookings = Booking.get_order_by_user(user)
  
  params={'bookings':bookings}
  return render(request,'myorder.html',params)  

def booking(request):
  if request.user.is_anonymous:
     return redirect("/sign")
  if request.method == "POST":
    user = request.session.get('user')
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    des = request.POST.get('des')
    address = request.POST.get('address')
    city = request.POST.get('city')
    state = request.POST.get('state')
    pincode = request.POST.get('pincode')
    booking_date = request.POST.get('booking_date')
    booking = Booking(user=user, name=name, email=email, phone=phone,des=des, booking_date=booking_date, order_date=datetime.today(), address=address, city=city, state=state, pincode=pincode)
    booking.save()
    messages.success(request,'Your booking Successfilly!!!')
  return render(request,'booking.html')

def reviews(request):
  reviews = Review.objects.all()
  params={'reviews':reviews}

  return render(request,'reviews.html',params)

def postreview(request):
  if request.user.is_anonymous:
     return redirect("/sign")
  if request.method == "POST":
    user = request.session.get('user')
    rating = request.POST.get('rating')
    review_msg = request.POST.get('review_msg')
    image = request.POST.get('image')
    review = Review(user=user, rating=rating, review_msg=review_msg, image=image, date=datetime.today())
    review.save()
    messages.success(request,'Your review Successfilly Post!!!')

  return render(request,'postreview.html')
    




    