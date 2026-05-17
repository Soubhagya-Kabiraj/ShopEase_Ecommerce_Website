"""
Reviews views — Add product review.
"""
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Review
from .forms import ReviewForm
from products.models import Product


@login_required
def add_review_view(request, product_id):
    """Add or update a review for a product."""
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        # Check if user already has a review
        existing_review = Review.objects.filter(product=product, user=request.user).first()

        if existing_review:
            # Update existing review
            form = ReviewForm(request.POST, instance=existing_review)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your review has been updated!')
        else:
            # Create new review
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.user = request.user
                review.product = product
                review.save()
                messages.success(request, 'Thank you for your review!')

    return redirect(product.get_absolute_url())
