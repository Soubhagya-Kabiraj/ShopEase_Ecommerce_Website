"""
Orders forms — Checkout / shipping address form.
"""
from django import forms
from .models import Order


class CheckoutForm(forms.ModelForm):
    """Shipping address form for checkout."""
    class Meta:
        model = Order
        fields = ['full_name', 'email', 'phone', 'address', 'city', 'state', 'zipcode']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Street address'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}),
            'zipcode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ZIP / Postal code'}),
        }
