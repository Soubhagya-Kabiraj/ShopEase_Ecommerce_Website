"""
Wishlist views — View wishlist, add/remove products.
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Wishlist
from products.models import Product


@login_required
def wishlist_view(request):
    """Display the user's wishlist."""
    wishlist_items = Wishlist.objects.filter(user=request.user).select_related('product')
    return render(request, 'wishlist/wishlist.html', {'wishlist_items': wishlist_items})


@login_required
def add_to_wishlist_view(request, product_id):
    """Add a product to the wishlist."""
    product = get_object_or_404(Product, id=product_id, is_active=True)
    wishlist_item, created = Wishlist.objects.get_or_create(
        user=request.user, product=product
    )

    if created:
        messages.success(request, f'"{product.name}" added to your wishlist!')
    else:
        messages.info(request, f'"{product.name}" is already in your wishlist.')

    next_url = request.GET.get('next', request.META.get('HTTP_REFERER', 'wishlist:wishlist'))
    return redirect(next_url)


@login_required
def remove_from_wishlist_view(request, item_id):
    """Remove a product from the wishlist."""
    wishlist_item = get_object_or_404(Wishlist, id=item_id, user=request.user)
    product_name = wishlist_item.product.name
    wishlist_item.delete()
    messages.success(request, f'"{product_name}" removed from your wishlist.')
    return redirect('wishlist:wishlist')
