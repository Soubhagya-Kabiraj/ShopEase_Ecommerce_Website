"""
Products context processor — Inject categories into all templates.
"""
from .models import Category


def categories_processor(request):
    """Make all categories available in every template for nav dropdown."""
    return {
        'all_categories': Category.objects.all()
    }
