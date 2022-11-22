from decimal import Decimal
from django.conf import settings
from inventory.models import Product
from cart.models import CartItem, ShoppingCart
from django.contrib.sessions.backends.db import SessionStore


class Cart():
    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.ss = SessionStore()
        #self.session = request.session
        cart_key = self.ss.session_key
        if not cart_key:
            cart_key = self.ss.create()


        cart = request.session.get(cart_key)
        if not cart:
    #        # save an empty cart in the session
            cart = request.session[cart_key] = {}
        self.cart = cart

    '''
    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()
        #item = Product.objects.get(id=product.id)
        #cart_item = CartItem.objects.create(product=item, quantity=1, cart=self.cart)
        print(self.cart, product_id)
    '''

    '''
    def add(self, product):
        item = Product.objects.get(id=product.id)
        cart_item = CartItem.objects.create(product=item, quantity=1)
        cart_item.save()
    '''


    def save(self):
    #    self.cart = self.cart
        self.ss.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[1]
        self.session.modified = True