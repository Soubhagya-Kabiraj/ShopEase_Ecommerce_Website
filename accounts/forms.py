"""
Accounts forms — Registration, Login, Profile Update forms.
"""
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile


class UserRegistrationForm(UserCreationForm):
    """Custom user registration form with email field."""
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Email address'}
    ))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'First name'}
    ))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Last name'}
    ))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control', 'placeholder': 'Username'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control', 'placeholder': 'Password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control', 'placeholder': 'Confirm password'
        })


class UserLoginForm(AuthenticationForm):
    """Custom login form with Bootstrap styling."""
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username'}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}
    ))


class UserUpdateForm(forms.ModelForm):
    """Form to update User fields (username, email, name)."""
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}
    ))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ProfileUpdateForm(forms.ModelForm):
    """Form to update Profile fields (phone, address, avatar)."""
    class Meta:
        model = Profile
        fields = ['avatar', 'phone', 'address', 'city', 'state', 'zipcode']
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Street address'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}),
            'zipcode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ZIP Code'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control'}),
        }
