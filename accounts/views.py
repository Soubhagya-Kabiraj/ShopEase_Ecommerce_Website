"""
Accounts views — Registration, Login, Logout, Profile, Edit Profile.
"""
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordResetForm
from .forms import UserRegistrationForm, UserLoginForm, UserUpdateForm, ProfileUpdateForm


def register_view(request):
    """Handle user registration."""
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome to ShopEase, {user.first_name}! Your account has been created.')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    """Handle user login."""
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.first_name or user.username}!')
                # Redirect to 'next' param if exists, otherwise home
                next_url = request.GET.get('next', 'home')
                return redirect(next_url)
        messages.error(request, 'Invalid username or password.')
    else:
        form = UserLoginForm()

    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    """Handle user logout."""
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home')


@login_required
def profile_view(request):
    """Display user profile page."""
    return render(request, 'accounts/profile.html')


@login_required
def edit_profile_view(request):
    """Handle profile editing."""
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('accounts:profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'accounts/edit_profile.html', context)


def forgot_password_view(request):
    """Handle forgot password (uses Django's built-in password reset)."""
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(request=request)
            messages.success(request, 'Password reset instructions have been sent to your email.')
            return redirect('accounts:login')
    else:
        form = PasswordResetForm()

    return render(request, 'accounts/forgot_password.html', {'form': form})
