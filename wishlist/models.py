"""
Wishlist models — User's saved products.
"""
from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Wishlist(models.Model):
    """A wishlist item linking a user to a product they want to save."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlist')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='wishlisted_by')
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')
        ordering = ['-added_at']
        verbose_name = 'Wishlist Item'
        verbose_name_plural = 'Wishlist Items'

    def __str__(self):
        return f'{self.user.username} — {self.product.name}'
