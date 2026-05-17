"""
Products URL configuration.
"""
from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('products/', views.product_list_view, name='product_list'),
    path('products/add/', views.product_create_view, name='product_create'),
    path('products/<slug:slug>/', views.product_detail_view, name='product_detail'),
    path('products/<slug:slug>/edit/', views.product_update_view, name='product_update'),
    path('products/<slug:slug>/delete/', views.product_delete_view, name='product_delete'),
    path('category/<slug:slug>/', views.category_products_view, name='category'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
]
