"""
Orders models — Order and OrderItem for checkout & order management.
"""
from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Order(models.Model):
    """Customer order with shipping details and status tracking."""

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
    ]

    PAYMENT_CHOICES = [
        ('COD', 'Cash on Delivery'),
        ('Stripe', 'Stripe (Card/UPI)'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    # Shipping address fields
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    # Order details
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES, default='COD')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    is_paid = models.BooleanField(default=False)
    stripe_session_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f'Order #{self.id} by {self.user.username}'

    @property
    def order_number(self):
        return f'SE-{self.id:06d}'


class OrderItem(models.Model):
    """Individual product within an order."""
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    product_name = models.CharField(max_length=300)  # Preserve name even if product deleted
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.quantity}x {self.product_name}'

    @property
    def subtotal(self):
        return self.price * self.quantity
