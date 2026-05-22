<img width="1888" height="911" alt="Screenshot 2026-05-22 151512" src="https://github.com/user-attachments/assets/e22f2649-b9f3-4d58-a462-82a40b87bc8f" /><div align="center">

# 🛒 ShopEase
### A Modern Django E-Commerce Website

<img src="https://img.shields.io/badge/Django-Framework-green?style=for-the-badge&logo=django">
<img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/SQLite-Database-lightblue?style=for-the-badge&logo=sqlite">
<img src="https://img.shields.io/badge/Bootstrap-5-purple?style=for-the-badge&logo=bootstrap">
<img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge">

---

### Shop smarter. Shop faster. Shop easier.

A fully responsive E-Commerce web application built using Django with essential shopping features including authentication, product management, cart, wishlist, checkout, orders, and reviews.

</div>

---

# 📖 Overview

ShopEase is a complete Django-based e-commerce application designed with a clean UI and user-friendly shopping experience. Users can browse products, search items, manage carts, save wishlists, place orders, and track purchases easily.

The project follows Django’s MVT architecture and focuses on scalability, maintainability, and clean coding practices.

---

# ✨ Features

## 👤 Authentication System

- User Registration
- User Login
- Logout
- Forgot Password
- User Profile Management
- Edit Profile

---

## 📦 Product Management

- Add Products
- Update Products
- Delete Products
- Product Details
- Product Images
- Product Categories
- Latest Products Section
- Stock Management

---

## 🔍 Search & Filtering

- Search Products
- Category Filtering
- Price Sorting
- Product Listing Page

---

## 🛒 Shopping Cart

- Add to Cart
- Remove from Cart
- Update Product Quantity
- Automatic Total Price Calculation

---

## ❤️ Wishlist

- Add Products to Wishlist
- Remove Wishlist Items
- Save Products for Later

---

## 💳 Checkout System

- Shipping Address
- Order Summary
- Cash on Delivery

---

## 📜 Order Management

- Order History
- Order Tracking

Order Status:

- Pending
- Shipped
- Delivered

---

## ⭐ Review System

- Product Ratings
- Customer Reviews

---

## ⚙️ Admin Dashboard

Admin can manage:

- Users
- Products
- Categories
- Orders
- Reviews

---

# 🏗️ Project Structure

```bash
ShopEase/
│
├── accounts/
├── products/
├── cart/
├── wishlist/
├── orders/
├── reviews/
├── templates/
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── media/
├── screenshots/
├── ShopEase/
├── manage.py
├── requirements.txt
└── README.md
```

---

# 🛠️ Tech Stack

| Technology | Usage |
|------------|--------|
| Python | Backend |
| Django | Web Framework |
| SQLite | Database |
| HTML | Structure |
| CSS | Styling |
| Bootstrap 5 | Responsive UI |
| JavaScript | Dynamic Features |

---

# 🚀 Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/ShopEase.git
```

---

## 2️⃣ Move into Project Directory

```bash
cd ShopEase
```

---

## 3️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate Environment:

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5️⃣ Apply Migrations

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

---

## 6️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

---

## 7️⃣ Run Development Server

```bash
python manage.py runserver
```

Open in browser:

```bash
http://127.0.0.1:8000/
```

---

# 📷 Website Screenshots

<div align="center">

| Home Page | Product List |
|------------|---------------|
| <img width="1888" height="911" alt="Screenshot 2026-05-22 151512" src="https://github.com/user-attachments/assets/0327518a-f869-4e9b-b7d0-624e3321f8d6" /> | <img width="1890" height="908" alt="Screenshot 2026-05-22 151605" src="https://github.com/user-attachments/assets/78d7692e-aa0e-45ae-9c6d-5522e6b3645f" /> |

| Product Detail | Latest Products |
|-----------------|-----------------|
| <img width="1427" height="911" alt="Screenshot 2026-05-22 152847" src="https://github.com/user-attachments/assets/c00ca95c-e44e-4327-bb12-eee99a1ba4bc" /> | <img width="1890" height="913" alt="Screenshot 2026-05-22 151820" src="https://github.com/user-attachments/assets/b8189551-1d33-4cca-8039-9e075190e4da" /> |

| Shop Categories | Cart |
|------------------|------|
| <img width="1691" height="916" alt="image" src="https://github.com/user-attachments/assets/da9cb2ce-4bdf-42b7-90f2-0feff5f38dc3" /> | <img width="1882" height="912" alt="Screenshot 2026-05-22 151857" src="https://github.com/user-attachments/assets/64580e1a-92fa-4a74-b5ea-8cdc90d4eee3" /> |

| Wishlist | Checkout |
|------------|-----------|
| <img width="1882" height="913" alt="Screenshot 2026-05-22 151943" src="https://github.com/user-attachments/assets/03ae8ced-3e42-470a-b67a-bfc353721631" /> | <img width="1465" height="910" alt="Screenshot 2026-05-22 153041" src="https://github.com/user-attachments/assets/4891e6ea-3e73-452f-94f1-1078e126041e" /> |

| User Profile |
|---------------|
| <img width="1719" height="917" alt="Screenshot 2026-05-22 153951" src="https://github.com/user-attachments/assets/fa42b22c-a7bc-4f1e-b320-e867715564a1" /> |

</div>

---

# 📄 Website Pages

✅ Home Page  
✅ Product List Page  
✅ Product Detail Page  
✅ Latest Products Section  
✅ Shop Categories Page  
✅ Cart Page  
✅ Wishlist Page  
✅ Checkout Page  
✅ User Profile Page  
✅ Login Page  
✅ Register Page  
✅ Order History Page  
✅ About Page  
✅ Contact Page  

---

# 🔐 Future Improvements

- Discount Coupons
- Email Notifications
- Product Recommendation System
- Dark Mode
- AI Product Suggestions
- Sales Analytics Dashboard

---

# 🤝 Contribution

Contributions are welcome.

### Steps to Contribute

#### 1️⃣ Fork the Repository

#### 2️⃣ Create a Feature Branch

```bash
git checkout -b feature-name
```

#### 3️⃣ Commit Your Changes

```bash
git commit -m "Added new feature"
```

#### 4️⃣ Push Changes

```bash
git push origin feature-name
```

#### 5️⃣ Open a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

<div align="center">

### ⭐ If you like this project, give it a star ⭐

Made with ❤️ using Django

</div>
