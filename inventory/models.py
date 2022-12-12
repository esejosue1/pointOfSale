from django.db import models
from category.models import Category
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    product_name=models.CharField(max_length=200, unique=True)
    slug=models.SlugField(max_length=200, unique=True, null=True)
    description=models.TextField(max_length=500, blank=True)
    price=models.IntegerField(null=True)
    image = models.ImageField(upload_to="photos/products", null=True)
    stock = models.IntegerField(null=True)
    is_available=models.BooleanField(default=True,null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    add_quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.product_name

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    