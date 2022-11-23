from django.shortcuts import render, get_object_or_404
from inventory.models import Product

from cart.forms import CartAddProductForm
from cart.cart import Cart

#from inventory.models import Product    #import inventory model to use it here
from django.http import HttpResponse
def home(request):
    
    products=Product.objects.all().filter(is_available=True)

    context={
        "products":products,
    }
    return render(request, "index.html", context)


def cart(request):  
    cart = Cart(request)
    context={
        "cart":cart
    }
    return render(request, "cart.html", context)
def cart1(request):  
    return render(request, "cart1.html", )

'''
def cart(request):
    items=Cart(request)
    context={
        "cart":items
    }
    return render(request, "cart.html", context)
'''

'''
def product_list(request):
    products = Product.objects.filter(available=True)
    context = {'products': products}
    return render(request, 'shop/product/list.html', context)
'''

'''
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {'product': product, 'cart_product_form': cart_product_form}
    return render(request, 'shop/product/detail.html', context)
'''
def orders(request):
    return render(request, "place-order.html")
