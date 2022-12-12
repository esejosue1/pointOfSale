from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
from django.http import HttpResponse

# Create your views here.
def inventory(request, category_slug=None):
    categories=None
    products=None

    #display the products with a category
    if category_slug != None:
        categories=get_object_or_404(Category, slug=category_slug)
        products=Product.objects.filter(category=categories, is_available=True)
        product_count=products.count()
    #display the products with no category
    else:
        products=Product.objects.all().filter(is_available=True)
        product_count=products.count()


    #passing info to front end
    context={
        "products":products,
        "product_count":product_count
    }

    return render(request, 'temp/index.html', context)


def productDetail(request,category_slug, product_slug):
    #check if we get the product
    try:
        product=Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    content ={
        "product":product
    }
    return render(request, "temp/product.html", content)

def search(request):
    # if the keyword exist, get its value ['keyword]
    if 'search' in request.GET:
        keyword = request.GET['search']
        if keyword:
            # look for the whole description that matches the keyword
            products = Product.objects.order_by('-created_date').filter(Q(price__icontains=keyword) | Q(product_name__icontains=keyword))
            found = products.count()
    context = {
        'products': products,
        'product_count': found,
    }
    return render(request, 'temp/search.html',context)