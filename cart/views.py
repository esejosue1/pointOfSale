from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from inventory.models import Product
from cart.models import CartItem, ShoppingCart
from django.contrib import messages
from django.http import HttpResponseRedirect


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

    cart_item.quantity += 1
    cart_item.save()

    messages.success(request, f'{item.product_name} Has Been Added!')
    #eturn HttpResponseRedirect('cart:index')

    #return redirect("cart:cart_detail")
    return redirect('cart:index')

def index(request):
    
    products=Product.objects.all().filter(is_available=True)

    context={
        "products":products,
    }
    return render(request, "temp/index.html", context)

def cart_remove(request, product_id):
    item = get_object_or_404(Product, id=product_id)
    try:
        cart = ShoppingCart.objects.get(cart_id=_cart_id(request))
        cart_item = CartItem.objects.get(product=item, cart=cart)
        cart_item.delete()
    except ShoppingCart.DoesNotExist:
        print('remove failed')

    return redirect('cart:cart_detail')

def cart_increment(request, product_id):
    item = get_object_or_404(Product, id=product_id)
    try:
        cart = ShoppingCart.objects.get(cart_id=_cart_id(request))
        cart_item = CartItem.objects.get(product=item, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except ShoppingCart.DoesNotExist:
        print('increment failed')

    return redirect('cart:cart_detail')

def cart_decrement(request, product_id):
    item = get_object_or_404(Product, id=product_id)
    try:
        cart = ShoppingCart.objects.get(cart_id=_cart_id(request))
        cart_item = CartItem.objects.get(product=item, cart=cart)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_remove(request, product_id)
    except ShoppingCart.DoesNotExist:
        print('decrement failed')

    return redirect('cart:cart_detail')

def cart_detail(request):
    try:
        cart = ShoppingCart.objects.get(cart_id=_cart_id(request))
    except ShoppingCart.DoesNotExist:
        cart = ShoppingCart.objects.create(cart_id=_cart_id(request))
#    cart = ShoppingCart.objects.get(cart_id=_cart_id(request))
    cart_items = CartItem.objects.filter(is_active=True, cart=cart)

    cart_subtotal = sum(item.itemtotal for item in cart_items)
    cart_tax = cart_subtotal * (0.055) # tax rate (5.5%)
    cart_shipping = 10 # shipping rate (flat $10)
    cart_total = cart_subtotal + cart_tax + cart_shipping
    context = {
        'cart_items': cart_items,
        'cart_subtotal': '{:.2f}'.format(cart_subtotal),
        'cart_tax': '{:.2f}'.format(cart_tax),
        'cart_shipping': '{:.2f}'.format(cart_shipping),
        'cart_total': '{:.2f}'.format(cart_total),
    }
    
    return render(request, 'temp/cart.html', context)

 #home page for checkout form
def cart_to_orders(request):
    try:
        cart = ShoppingCart.objects.get(cart_id=_cart_id(request))
    except ShoppingCart.DoesNotExist:
        cart = ShoppingCart.objects.create(cart_id=_cart_id(request))
#    cart = ShoppingCart.objects.get(cart_id=_cart_id(request))
    cart_items = CartItem.objects.filter(is_active=True, cart=cart)

    cart_subtotal = sum(item.itemtotal for item in cart_items)
    cart_tax = cart_subtotal * (0.055) # tax rate (5.5%)
    cart_shipping = 10 # shipping rate (flat $10)
    cart_total = cart_subtotal + cart_tax + cart_shipping
    context = {
        'cart_items': cart_items,
        'cart_subtotal': '{:.2f}'.format(cart_subtotal),
        'cart_tax': '{:.2f}'.format(cart_tax),
        'cart_shipping': '{:.2f}'.format(cart_shipping),
        'cart_total': '{:.2f}'.format(cart_total),
    }
    return render(request, "temp/checkout.html", context)

def cart_add_decrement(request, product_id):
    item = get_object_or_404(Product, id=product_id)
    if item.add_quantity > 1:
        item.add_quantity -= 1
        item.save()

    context = {
        'product': item,
    }

    return render(request, 'temp/product.html', context)

def cart_add_increment(request, product_id):
    item = get_object_or_404(Product, id=product_id)
    item.add_quantity += 1
    item.save()

    context = {
        'product': item,
    }

    return render(request, 'temp/product.html', context)

def cart_add_quantity(request, product_id):
    item = get_object_or_404(Product, id=product_id)
    try:
        cart = ShoppingCart.objects.get(cart_id=_cart_id(request))
        cart_item = CartItem.objects.get(product=item, cart=cart)
        cart_item.quantity += item.add_quantity
        item.add_quantity = 1
        item.save()
        cart_item.save()

    except ShoppingCart.DoesNotExist:
        print('set quantity failed')

    return redirect('cart:cart_detail')
