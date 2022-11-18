from django.contrib import admin
from .models import CartItem

class CartAdmin(admin.ModelAdmin):
    list_display = ("product", "quantity", "is_active")

admin.site.register(CartItem, CartAdmin)