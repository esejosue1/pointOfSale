from django.shortcuts import render
from .models import Product

# Create your views here.
def inventory(request):
    products=Product.objects.all().filter(is_available=True)
    product_count=products.count()
    print(products.count())

    #passing info to front end
    context={
        "products":products,
        "product_count":product_count,
    }

    return render(request, 'templates/home.html', context)

