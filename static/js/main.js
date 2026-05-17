/* ===== ShopEase — Main JavaScript ===== */

document.addEventListener('DOMContentLoaded', function () {

    // ---------- Auto-dismiss alerts after 4 seconds ----------
    const alerts = document.querySelectorAll('.alert-dismissible');
    alerts.forEach(function (alert) {
        setTimeout(function () {
            const bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
            bsAlert.close();
        }, 4000);
    });

    // ---------- Navbar scroll effect ----------
    const navbar = document.getElementById('main-navbar');
    if (navbar) {
        window.addEventListener('scroll', function () {
            if (window.scrollY > 50) {
                navbar.classList.add('shadow-lg');
                navbar.style.padding = '0.3rem 0';
            } else {
                navbar.classList.remove('shadow-lg');
                navbar.style.padding = '0.6rem 0';
            }
        });
    }

    // ---------- Cart quantity update ----------
    const qtyForms = document.querySelectorAll('.qty-update-form');
    qtyForms.forEach(function (form) {
        const input = form.querySelector('.cart-qty-input');
        if (input) {
            input.addEventListener('change', function () {
                form.submit();
            });
        }
    });

    // ---------- Product card animation on scroll ----------
    const observerOptions = { threshold: 0.1, rootMargin: '0px 0px -50px 0px' };
    const observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-fade-in');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.product-card, .category-card, .order-card').forEach(function (el) {
        observer.observe(el);
    });

    // ---------- Star rating interactive (review form) ----------
    const ratingSelect = document.getElementById('id_rating');
    if (ratingSelect) {
        const starContainer = document.createElement('div');
        starContainer.className = 'star-rating-input d-flex gap-1 mb-2';
        for (let i = 1; i <= 5; i++) {
            const star = document.createElement('i');
            star.className = 'bi bi-star star-interactive';
            star.dataset.value = i;
            star.style.cursor = 'pointer';
            star.style.fontSize = '1.5rem';
            star.style.color = '#ddd';
            star.style.transition = 'color 0.2s';

            star.addEventListener('click', function () {
                ratingSelect.value = this.dataset.value;
                updateStars(starContainer, parseInt(this.dataset.value));
            });
            star.addEventListener('mouseenter', function () {
                updateStars(starContainer, parseInt(this.dataset.value));
            });
            starContainer.addEventListener('mouseleave', function () {
                updateStars(starContainer, parseInt(ratingSelect.value) || 0);
            });
            starContainer.appendChild(star);
        }
        ratingSelect.parentNode.insertBefore(starContainer, ratingSelect);
        ratingSelect.style.display = 'none';

        // Set initial stars
        if (ratingSelect.value) {
            updateStars(starContainer, parseInt(ratingSelect.value));
        }
    }

    function updateStars(container, value) {
        container.querySelectorAll('.star-interactive').forEach(function (star) {
            const v = parseInt(star.dataset.value);
            if (v <= value) {
                star.className = 'bi bi-star-fill star-interactive';
                star.style.color = '#f5a623';
            } else {
                star.className = 'bi bi-star star-interactive';
                star.style.color = '#ddd';
            }
        });
    }

    // ---------- Confirm delete ----------
    const deleteForms = document.querySelectorAll('.delete-confirm-form');
    deleteForms.forEach(function (form) {
        form.addEventListener('submit', function (e) {
            if (!confirm('Are you sure you want to delete this item?')) {
                e.preventDefault();
            }
        });
    });

    // ---------- Smooth scroll for anchor links ----------
    document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
        anchor.addEventListener('click', function (e) {
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });
});
