from django.shortcuts import render
from inventory.models import Product

#from inventory.models import Product    #import inventory model to use it here
from django.http import HttpResponse
def home(request):
    
    products=Product.objects.all().filter(is_available=True)

    context={
        "products":products,
    }
    return render(request, "home.html", context)

def orders(request):
    return render(request, "place-order.html")