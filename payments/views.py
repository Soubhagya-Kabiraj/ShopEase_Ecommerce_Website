"""
Payments views — Stripe Checkout Session creation, success/cancel callbacks, webhook.
"""
import json
import stripe
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from orders.models import Order, OrderItem
from orders.forms import CheckoutForm
from cart.models import Cart

stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
@require_POST
def create_checkout_session(request):
    """Create a Stripe Checkout Session and redirect to Stripe's hosted page."""
    try:
        cart = request.user.cart
        cart_items = cart.items.select_related('product').all()
    except Cart.DoesNotExist:
        messages.error(request, 'Your cart is empty.')
        return redirect('cart:cart_detail')

    if not cart_items.exists():
        messages.error(request, 'Your cart is empty. Add some products before checkout.')
        return redirect('cart:cart_detail')

    form = CheckoutForm(request.POST)
    if not form.is_valid():
        messages.error(request, 'Please correct the errors in your shipping details.')
        return redirect('orders:checkout')

    # Create Order (unpaid, payment_method='Stripe')
    order = form.save(commit=False)
    order.user = request.user
    order.total_amount = cart.total_price
    order.payment_method = 'Stripe'
    order.is_paid = False
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

    # Build Stripe line items
    line_items = []
    for item in cart_items:
        line_items.append({
            'price_data': {
                'currency': 'inr',
                'product_data': {
                    'name': item.product.name,
                    'description': f'Qty: {item.quantity}',
                },
                'unit_amount': int(item.product.price * 100),  # Stripe uses paise/cents
            },
            'quantity': item.quantity,
        })

    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url=request.build_absolute_uri('/payments/success/') + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=request.build_absolute_uri('/payments/cancel/') + f'?order_id={order.id}',
            metadata={
                'order_id': str(order.id),
                'user_id': str(request.user.id),
            },
        )

        # Save session ID on the order
        order.stripe_session_id = checkout_session.id
        order.save()

        return redirect(checkout_session.url)

    except stripe.error.StripeError as e:
        # If Stripe fails, delete the order and show error
        order.delete()
        messages.error(request, f'Payment error: {str(e)}')
        return redirect('orders:checkout')


@login_required
def payment_success(request):
    """Handle successful Stripe payment redirect."""
    session_id = request.GET.get('session_id')
    if not session_id:
        messages.error(request, 'Invalid payment session.')
        return redirect('home')

    try:
        session = stripe.checkout.Session.retrieve(session_id)
    except stripe.error.StripeError:
        messages.error(request, 'Could not verify payment. Please contact support.')
        return redirect('home')

    order_id = session.metadata.get('order_id')
    if not order_id:
        messages.error(request, 'Order not found.')
        return redirect('home')

    order = get_object_or_404(Order, id=order_id, user=request.user)

    # Mark as paid if payment succeeded
    if session.payment_status == 'paid' and not order.is_paid:
        order.is_paid = True
        order.save()

        # Reduce stock
        for item in order.items.select_related('product').all():
            if item.product:
                item.product.stock -= item.quantity
                item.product.save()

        # Clear the cart
        try:
            cart = request.user.cart
            cart.items.all().delete()
        except Cart.DoesNotExist:
            pass

    order_items = order.items.select_related('product').all()
    context = {
        'order': order,
        'order_items': order_items,
    }
    return render(request, 'payments/payment_success.html', context)


@login_required
def payment_cancel(request):
    """Handle cancelled Stripe payment."""
    order_id = request.GET.get('order_id')
    if order_id:
        try:
            order = Order.objects.get(id=order_id, user=request.user, is_paid=False, payment_method='Stripe')
            # Delete the unpaid order and its items
            order.items.all().delete()
            order.delete()
        except Order.DoesNotExist:
            pass

    messages.warning(request, 'Payment was cancelled. Your cart items are still saved.')
    return render(request, 'payments/payment_cancel.html')


@csrf_exempt
@require_POST
def stripe_webhook(request):
    """Handle Stripe webhook events for async payment confirmation."""
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    webhook_secret = getattr(settings, 'STRIPE_WEBHOOK_SECRET', None)

    if not webhook_secret:
        return HttpResponse(status=400)

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, webhook_secret)
    except (ValueError, stripe.error.SignatureVerificationError):
        return HttpResponse(status=400)

    # Handle checkout.session.completed
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        order_id = session.get('metadata', {}).get('order_id')

        if order_id:
            try:
                order = Order.objects.get(id=order_id)
                if not order.is_paid:
                    order.is_paid = True
                    order.save()

                    # Reduce stock
                    for item in order.items.select_related('product').all():
                        if item.product:
                            item.product.stock -= item.quantity
                            item.product.save()

                    # Clear the cart
                    try:
                        cart = order.user.cart
                        cart.items.all().delete()
                    except Cart.DoesNotExist:
                        pass
            except Order.DoesNotExist:
                pass

    return HttpResponse(status=200)
