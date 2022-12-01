from django.db import models
from inventory.models import Product

class ShoppingCart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.cart_id

    def remove(self, product_id):
        """
        Remove a product from the cart.
        """
        #product_id = str(product.id)
        del product_id

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    @property
    def itemtotal(self):
        return self.product.price*self.quantity

    @property
    def carttotal(self):
        return sum(self.itemtotal for self.product in self.cart)

    def __unicode__(self):
        return self.product
        