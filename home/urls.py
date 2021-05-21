from django.contrib import admin
from django.urls import path
from home import views
from django.contrib.auth import views as auth_views



urlpatterns = [
  
    path("", views.index ,name='home'),
    path("about", views.about ,name='about'),
    path("contact", views.contact ,name='contact'),
    path("sign", views.sign ,name='sign'),
    path("signout", views.signout ,name='signout'),
    path("registration", views.registration ,name='registration'),   
    path("profile", views.profile ,name='profile'),
    path("booking", views.booking, name='booking'),
    path("myorder", views.myorder, name='myorder'),
    path("reviews", views.reviews, name='reviews'),
    path("postreview", views.postreview, name='postreview'),

    #password reset manual 
    # path("reset_password",auth_views.PasswordResetView.as_view(), name="reset_password"),

    # path("reset_password_sent", auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),

    # path("reset/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),

    # path("reset_password_complete/",auth_views.PasswordResetCompleteView.as_view(),name="Password_reset_complete")

    
]
