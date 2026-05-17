"""
Cart views — View cart, add/remove/update items.
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Cart, CartItem
from products.models import Product


@login_required
def cart_detail_view(request):
    """Display the user's shopping cart."""
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.select_related('product').all()

    context = {
        'cart': cart,
        'cart_items': cart_items,
    }
    return render(request, 'cart/cart.html', context)


@login_required
def add_to_cart_view(request, product_id):
    """Add a product to the cart."""
    product = get_object_or_404(Product, id=product_id, is_active=True)
    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, item_created = CartItem.objects.get_or_create(
        cart=cart, product=product
    )

    if not item_created:
        # Item already in cart — increment quantity
        if cart_item.quantity < product.stock:
            cart_item.quantity += 1
            cart_item.save()
            messages.success(request, f'Updated quantity for "{product.name}".')
        else:
            messages.warning(request, f'Maximum available stock reached for "{product.name}".')
    else:
        if product.stock < 1:
            cart_item.delete()
            messages.error(request, f'"{product.name}" is out of stock.')
        else:
            messages.success(request, f'"{product.name}" added to cart!')

    # Redirect back to referring page or cart
    next_url = request.GET.get('next', request.META.get('HTTP_REFERER', 'cart:cart_detail'))
    return redirect(next_url)


@login_required
def remove_from_cart_view(request, item_id):
    """Remove an item from the cart."""
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    product_name = cart_item.product.name
    cart_item.delete()
    messages.success(request, f'"{product_name}" removed from cart.')
    return redirect('cart:cart_detail')


@login_required
def update_cart_view(request, item_id):
    """Update the quantity of a cart item."""
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        if quantity < 1:
            cart_item.delete()
            messages.success(request, f'"{cart_item.product.name}" removed from cart.')
        elif quantity > cart_item.product.stock:
            messages.warning(request, f'Only {cart_item.product.stock} available in stock.')
            cart_item.quantity = cart_item.product.stock
            cart_item.save()
        else:
            cart_item.quantity = quantity
            cart_item.save()
            messages.success(request, 'Cart updated.')

    return redirect('cart:cart_detail')
