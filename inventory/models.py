from django.db import models

# Create your models here.
class Product(models.Model):
    product_name=models.CharField(max_length=200, unique=True)
    price=models.IntegerField(null=True)
    image = models.ImageField(upload_to="photos/inventory", null=True)
    stock = models.IntegerField(null=True)
    is_available=models.BooleanField(default=True,null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name