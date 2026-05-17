"""
Products views — Home, Product listing, detail, search, filter, CRUD.
"""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category
from reviews.models import Review
from reviews.forms import ReviewForm


def home_view(request):
    """Home page with featured and latest products."""
    featured_products = Product.objects.filter(is_featured=True, is_active=True)[:8]
    latest_products = Product.objects.filter(is_active=True)[:8]
    categories = Category.objects.all()[:6]

    context = {
        'featured_products': featured_products,
        'latest_products': latest_products,
        'categories': categories,
    }
    return render(request, 'home.html', context)


def product_list_view(request):
    """Product listing with search, category filter, and price sort."""
    products = Product.objects.filter(is_active=True)

    # Search by name
    query = request.GET.get('q', '')
    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    # Filter by category
    category_slug = request.GET.get('category', '')
    category = None
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    # Sort by price
    sort = request.GET.get('sort', '')
    if sort == 'price_low':
        products = products.order_by('price')
    elif sort == 'price_high':
        products = products.order_by('-price')
    elif sort == 'newest':
        products = products.order_by('-created_at')
    elif sort == 'name':
        products = products.order_by('name')

    context = {
        'products': products,
        'query': query,
        'current_category': category,
        'current_sort': sort,
    }
    return render(request, 'products/product_list.html', context)


def product_detail_view(request, slug):
    """Single product detail page with reviews."""
    product = get_object_or_404(Product, slug=slug, is_active=True)
    reviews = product.reviews.all()
    related_products = Product.objects.filter(
        category=product.category, is_active=True
    ).exclude(pk=product.pk)[:4]

    # Check if user already reviewed
    user_review = None
    if request.user.is_authenticated:
        user_review = Review.objects.filter(product=product, user=request.user).first()

    # Review form
    review_form = ReviewForm()

    context = {
        'product': product,
        'reviews': reviews,
        'related_products': related_products,
        'review_form': review_form,
        'user_review': user_review,
    }
    return render(request, 'products/product_detail.html', context)


def category_products_view(request, slug):
    """Show products for a specific category."""
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category, is_active=True)

    # Sort
    sort = request.GET.get('sort', '')
    if sort == 'price_low':
        products = products.order_by('price')
    elif sort == 'price_high':
        products = products.order_by('-price')
    elif sort == 'newest':
        products = products.order_by('-created_at')

    context = {
        'category': category,
        'products': products,
        'current_sort': sort,
    }
    return render(request, 'products/category_products.html', context)


@staff_member_required
def product_create_view(request):
    """Create a new product (staff only)."""
    from .forms import ProductForm
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, f'Product "{product.name}" created successfully!')
            return redirect(product.get_absolute_url())
    else:
        form = ProductForm()

    return render(request, 'products/product_form.html', {'form': form, 'title': 'Add Product'})


@staff_member_required
def product_update_view(request, slug):
    """Update an existing product (staff only)."""
    from .forms import ProductForm
    product = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()
            messages.success(request, f'Product "{product.name}" updated successfully!')
            return redirect(product.get_absolute_url())
    else:
        form = ProductForm(instance=product)

    return render(request, 'products/product_form.html', {'form': form, 'title': 'Edit Product'})


@staff_member_required
def product_delete_view(request, slug):
    """Delete a product (staff only)."""
    product = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        name = product.name
        product.delete()
        messages.success(request, f'Product "{name}" deleted.')
        return redirect('products:product_list')

    return render(request, 'products/product_confirm_delete.html', {'product': product})


def about_view(request):
    """About page."""
    return render(request, 'about.html')


def contact_view(request):
    """Contact page."""
    if request.method == 'POST':
        messages.success(request, 'Thank you for contacting us! We will get back to you soon.')
        return redirect('contact')
    return render(request, 'contact.html')
