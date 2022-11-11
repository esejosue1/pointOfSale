from django.db import models
from inventory.models import Product

class ShoppingCart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.cart_id

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE, null=True)
    # manytomanyfield is for a product to have other variations for the same prsoduct
    quantity = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    # show current total of specific product items
    def subtotal(self):
        return self.product.price*self.quantity

    def __unicode__(self):
        return self.product
        