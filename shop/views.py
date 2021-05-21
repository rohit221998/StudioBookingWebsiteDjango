from django.shortcuts import render , HttpResponse, redirect
from .models import Product

# Create your views here.

def index(request):
    products = Product.objects.all()
    n=len(products) 
    print('Your username is:',request.session.get('user'))
    params={'range':range(n),'products':products}
    if request.method == "POST":
        product = request.POST.get('product')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                cart[product] = quantity+1
            else:
                cart[product] = 1    
        else:
            cart ={}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart',request.session['cart'])
    return render(request,'shop/index.html',params)
def orderstatus(request):

    return HttpResponse("this is orderstatus page") 

def productview(request):

 return HttpResponse("this is productview page") 

def checkout(request):
 return render(request,'shop/checkout.html')
