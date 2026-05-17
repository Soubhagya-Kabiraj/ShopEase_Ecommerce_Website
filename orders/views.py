"""
Orders views — Checkout, Order History, Order Detail.
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Order, OrderItem
from .forms import CheckoutForm
from cart.models import Cart


@login_required
def checkout_view(request):
    """Checkout page with shipping form and order summary."""
    try:
        cart = request.user.cart
        cart_items = cart.items.select_related('product').all()
    except Cart.DoesNotExist:
        messages.error(request, 'Your cart is empty.')
        return redirect('cart:cart_detail')

    if not cart_items.exists():
        messages.error(request, 'Your cart is empty. Add some products before checkout.')
        return redirect('cart:cart_detail')

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.total_amount = cart.total_price
            order.payment_method = 'COD'
            order.save()

            # Create order items from cart
            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    product_name=item.product.name,
                    quantity=item.quantity,
                    price=item.product.price,
                )
                # Reduce stock
                item.product.stock -= item.quantity
                item.product.save()

            # Clear the cart
            cart_items.delete()

            messages.success(request, f'Order {order.order_number} placed successfully! Payment: Cash on Delivery.')
            return redirect('orders:order_detail', order_id=order.id)
    else:
        # Pre-fill from profile if available
        initial = {}
        if hasattr(request.user, 'profile'):
            profile = request.user.profile
            initial = {
                'full_name': f'{request.user.first_name} {request.user.last_name}'.strip(),
                'email': request.user.email,
                'phone': profile.phone,
                'address': profile.address,
                'city': profile.city,
                'state': profile.state,
                'zipcode': profile.zipcode,
            }
        form = CheckoutForm(initial=initial)

    context = {
        'form': form,
        'cart': cart,
        'cart_items': cart_items,
    }
    return render(request, 'orders/checkout.html', context)


@login_required
def order_history_view(request):
    """Display all orders for the current user."""
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_history.html', {'orders': orders})


@login_required
def order_detail_view(request, order_id):
    """Display details of a single order."""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order_items = order.items.select_related('product').all()

    context = {
        'order': order,
        'order_items': order_items,
    }
    return render(request, 'orders/order_detail.html', context)
