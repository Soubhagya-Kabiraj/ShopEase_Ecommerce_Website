"""
Root URL configuration for ShopEase project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from products import views as product_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Root-level named URLs (so templates can use {% url 'home' %} etc.)
    path('', product_views.home_view, name='home'),
    path('about/', product_views.about_view, name='about'),
    path('contact/', product_views.contact_view, name='contact'),
    # Namespaced app URLs
    path('', include('products.urls')),
    path('accounts/', include('accounts.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('wishlist/', include('wishlist.urls')),
    path('reviews/', include('reviews.urls')),
    path('payments/', include('payments.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Customize admin site
admin.site.site_header = 'ShopEase Administration'
admin.site.site_title = 'ShopEase Admin'
admin.site.index_title = 'Dashboard'
