from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from inventory.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from cart.models import CartItem, ShoppingCart

def _cart_id(request):
    return request.session.session_key or request.session.create()

@require_POST
def cart_add(request, product_id):
    item = get_object_or_404(Product, id=product_id)
    try:
        cart = ShoppingCart.objects.get(cart_id=_cart_id(request))
    except ShoppingCart.DoesNotExist:
        cart = ShoppingCart.objects.create(cart_id=_cart_id(request))
    cart.save()

    try:
        cart_item = CartItem.objects.get(cart=cart, product=item)
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(cart=cart, product=item)
    #form = CartAddProductForm(request.POST)
    #if form.is_valid():
    #    cd = form.cleaned_data
    cart_item.quantity += 1
    cart_item.save()
    print(product_id, item, cart_item.quantity, cart_item)
    return redirect("cart:cart_detail")


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

'''
def cart_detail(request):
    cart = ShoppingCart.objects.filter()
    context = {'cart':cart}
    return render(request, 'cart', context)
'''

def cart_detail(request):
    cart = ShoppingCart.objects.get(cart_id=_cart_id(request))
    cart_items = CartItem.objects.filter(is_active=True, cart=cart)
    #for item in cart_items:
    #    print(item.product.product_name)
    #for item in cart_items:
    #    item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    context = {
        'cart_items': cart_items
    }
    
    return render(request, 'home.html', context)
