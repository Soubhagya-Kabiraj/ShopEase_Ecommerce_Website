"""
Products admin — Customized admin for Product and Category management.
"""
from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock', 'is_featured', 'is_active', 'created_at']
    list_filter = ['category', 'is_featured', 'is_active', 'created_at']
    list_editable = ['price', 'stock', 'is_featured', 'is_active']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 25
