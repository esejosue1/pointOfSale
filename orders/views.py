from django.shortcuts import render
from .forms import orderForm
from .models import Order
# Create your views here.


def completeOrder(request):
    if request.method == "POST": 
        form = orderForm(request.POST)
        if form.is_valid():
            data = Order()
            data.first_name = form.cleaned_data["first_name"]
            data.last_name = form.cleaned_data["last_name"]
            data.phone = form.cleaned_data["phone"]
            data.email = form.cleaned_data["email"]
            data.address = form.cleaned_data["address"]
            data.address2 = form.cleaned_data["address2"]
            data.state = form.cleaned_data["state"]
            data.city = form.cleaned_data["city"]
            data.zip = form.cleaned_data["zip"]
        
            data.save()
        return render(request, "checkout.html")

    else:
        return render(request, "index.html")
 
def orders(request):
    return render(request, "checkout.html")
