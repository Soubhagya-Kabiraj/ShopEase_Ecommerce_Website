"""
Reviews models — Product ratings and reviews.
"""
from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    """Product review with star rating."""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text='Rating from 1 to 5 stars'
    )
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('product', 'user')  # One review per product per user
        ordering = ['-created_at']
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f'{self.user.username} — {self.product.name} ({self.rating}★)'
