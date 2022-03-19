import email
from django import forms


class CustomPaymentForm(forms.Form):
    amount = forms.IntegerField()
    name = forms.CharField(max_length=100)
    phone = forms.IntegerField()
    email = forms.EmailField()