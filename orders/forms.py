from django import forms
from .models import Order
class orderForm(forms.ModelForm):
    class meta:
        models = Order
        fields = ["first_name", "last_name", "phone","email",
        "address", "address2", "state","city","zip"
         ]