"""
Cart context processor — Inject cart item count into all templates.
"""


def cart_processor(request):
    """Make cart item count available in every template for the navbar badge."""
    cart_count = 0
    if request.user.is_authenticated:
        try:
            cart_count = request.user.cart.total_items
        except Exception:
            cart_count = 0
    return {'cart_count': cart_count}
