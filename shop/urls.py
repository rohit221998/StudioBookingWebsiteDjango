
from django.urls import path
from shop import views



urlpatterns = [
  
    path("", views.index ,name='ShopHome'),
    path("orderstatus", views.orderstatus ,name='OrderStatus'),
    path("productview",views.productview, name="ProductView"),
    path("checkout",views.checkout,name="CheckOut"),
    
]
