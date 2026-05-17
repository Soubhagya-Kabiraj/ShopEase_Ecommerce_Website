"""Seed script — populates database with sample categories and products."""
import os, django
os.environ['DJANGO_SETTINGS_MODULE'] = 'shopease.settings'
django.setup()

from products.models import Category, Product

# Categories
cats = {}
for name in ['Electronics', 'Fashion', 'Home & Kitchen', 'Books', 'Sports', 'Beauty']:
    obj, _ = Category.objects.get_or_create(name=name)
    cats[name] = obj
    print(f'  Category: {name}')

# Products
products_data = [
    ('Wireless Bluetooth Headphones', 'Premium noise-cancelling wireless headphones with 30-hour battery life, deep bass, and comfortable over-ear design. Perfect for music lovers and professionals.', 2499.00, 'Electronics', 50, True),
    ('Smart Fitness Watch', 'Track your health and fitness with heart rate monitoring, sleep tracking, GPS, and 7-day battery life. Water-resistant up to 50m.', 3999.00, 'Electronics', 35, True),
    ('USB-C Fast Charger 65W', 'Universal fast charger compatible with laptops, tablets, and smartphones. GaN technology for compact size and efficient charging.', 1299.00, 'Electronics', 100, False),
    ('Portable Bluetooth Speaker', 'Waterproof portable speaker with 360-degree sound, 12-hour playtime, and built-in microphone for calls.', 1799.00, 'Electronics', 60, False),
    ('Men\'s Casual Cotton Shirt', 'Premium cotton casual shirt with a modern slim fit. Available in multiple colors. Breathable and comfortable for all-day wear.', 899.00, 'Fashion', 200, True),
    ('Women\'s Running Shoes', 'Lightweight and breathable running shoes with cushioned sole for maximum comfort. Perfect for jogging and gym workouts.', 2199.00, 'Fashion', 80, True),
    ('Classic Leather Wallet', 'Genuine leather bi-fold wallet with RFID protection, multiple card slots, and a sleek minimalist design.', 649.00, 'Fashion', 150, False),
    ('Designer Sunglasses UV400', 'Polarized sunglasses with UV400 protection, lightweight frame, and scratch-resistant lenses. Unisex design.', 1199.00, 'Fashion', 90, False),
    ('Non-Stick Cookware Set (5 pcs)', 'Premium non-stick cookware set including frying pan, saucepan, kadai, tawa, and casserole. Induction compatible.', 2999.00, 'Home & Kitchen', 40, True),
    ('Automatic Coffee Maker', 'Programmable drip coffee maker with 12-cup capacity, built-in grinder, and keep-warm function.', 4599.00, 'Home & Kitchen', 25, False),
    ('LED Desk Lamp with USB Charging', 'Adjustable LED desk lamp with 5 brightness levels, USB charging port, and eye-care technology. Touch control.', 999.00, 'Home & Kitchen', 70, False),
    ('Stainless Steel Water Bottle 1L', 'Double-wall vacuum insulated bottle keeps drinks hot for 12 hrs and cold for 24 hrs. BPA-free and leak-proof.', 599.00, 'Home & Kitchen', 200, False),
    ('The Psychology of Money', 'Timeless lessons on wealth, greed, and happiness by Morgan Housel. One of the best-selling personal finance books.', 349.00, 'Books', 300, True),
    ('Atomic Habits by James Clear', 'An easy & proven way to build good habits and break bad ones. Over 10 million copies sold worldwide.', 399.00, 'Books', 250, False),
    ('Python Crash Course', 'A hands-on, project-based introduction to programming. Best-selling Python book for beginners.', 499.00, 'Books', 100, False),
    ('Yoga Mat Premium 6mm', 'Extra thick non-slip yoga mat with carrying strap. Perfect for yoga, pilates, and floor exercises.', 799.00, 'Sports', 120, True),
    ('Resistance Bands Set', 'Set of 5 resistance bands with different levels. Ideal for home workouts, physical therapy, and stretching.', 499.00, 'Sports', 200, False),
    ('Vitamin C Face Serum', 'Brightening face serum with 20% Vitamin C, hyaluronic acid, and vitamin E. For glowing, youthful skin.', 699.00, 'Beauty', 150, True),
    ('Natural Lip Balm Set (4 pack)', 'Organic lip balms in four flavors — vanilla, strawberry, mint, and honey. Moisturizing and long-lasting.', 299.00, 'Beauty', 300, False),
    ('Hair Growth Oil 200ml', 'Ayurvedic hair oil blend with coconut, amla, bhringraj, and castor oil. Promotes hair growth and reduces fall.', 449.00, 'Beauty', 180, False),
]

for name, desc, price, cat, stock, featured in products_data:
    Product.objects.get_or_create(
        name=name,
        defaults={
            'description': desc, 'price': price,
            'category': cats[cat], 'stock': stock, 'is_featured': featured,
        }
    )
    print(f'  Product: {name}')

print(f'\nDone! {Category.objects.count()} categories, {Product.objects.count()} products.')
