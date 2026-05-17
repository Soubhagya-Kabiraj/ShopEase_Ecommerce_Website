"""
Products forms — Product create/update form.
"""
from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """Form for creating and updating products."""
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'category', 'stock', 'is_featured', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Product description'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price', 'step': '0.01'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Stock quantity'}),
            'is_featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
