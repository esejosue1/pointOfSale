from django import forms
from .models import Order

#With this class, it enable us to grab information from a form in an html file
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order   #what model to point 
        fields = ["first_name", "last_name", "phone","email","address", "address2", "state","city","zip"]   #models we want to put data in