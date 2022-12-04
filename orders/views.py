from django.shortcuts import render,redirect
from .forms import OrderForm
from .models import Order
import datetime
# Create your views here.


def completeOrder(request):
    if request.method == "POST": 
        form = OrderForm(request.POST)
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
            data.ip = request.META.get('REMOTE_ADDR')
            data.order_total = 0
            data.tax = 0

            data.save()
            # order number
            yr = int(datetime.date.today().strftime('%Y'))
            dt = int(datetime.date.today().strftime('%d'))
            mt = int(datetime.date.today().strftime('%m'))
            d = datetime.date(yr, mt, dt)
            current_date = d.strftime("%Y%m%d")
            o_number = current_date + str(data.id)
            data.order_number = o_number
            data.save()
            return render(request, "checkout.html")
        else:
            print(form.errors)
       

 
def orders(request):
    return render(request, "checkout.html")
