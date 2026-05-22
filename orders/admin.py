"""
Orders admin — Customized admin for order management.
"""
from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['product', 'product_name', 'quantity', 'price', 'subtotal']

    def subtotal(self, obj):
        return obj.subtotal


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'user', 'full_name', 'total_amount', 'status', 'payment_method', 'is_paid', 'created_at']
    list_filter = ['status', 'payment_method', 'created_at']
    list_editable = ['status']
    search_fields = ['user__username', 'full_name', 'email']
    inlines = [OrderItemInline]
    list_per_page = 25
    readonly_fields = ['user', 'total_amount', 'created_at', 'updated_at', 'stripe_session_id']
