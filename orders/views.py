from django.shortcuts import render,redirect
from .forms import OrderForm
from .models import Order
import datetime
# Create your views here.



def completeOrder(request):
    #check if form is post
    form = OrderForm(request.POST)  #new var that holds the info from form.py
        
    if form.is_valid():     #if valid
 
        data = Order()      #var that match to the Order model

        #start inserting the data from the form into the Order model
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
        data.order_total = 0    #NEEDS FIX
        data.tax = 0            #NEEDS FIX

        data.save()     #save in database
        # get current time
        yr = int(datetime.date.today().strftime('%Y'))
        dt = int(datetime.date.today().strftime('%d'))
        mt = int(datetime.date.today().strftime('%m'))
        d = datetime.date(yr, mt, dt)
        current_date = d.strftime("%Y%m%d")
        o_number = current_date + str(data.id)
        data.order_number = o_number
        data.save()

        order = Order.objects.get(is_ordered=False, order_number=o_number)

        # values to be access from the html

        context = {
            'form': data,
        }
           
        return render(request, "confirmation.html", context)

    else:
        form = OrderForm(request.POST)
        return render(request, "index.html")
        #print(form.errors)  #error
        
       

 #home page for checkout form
def orders(request):
    return render(request, "checkout.html")



