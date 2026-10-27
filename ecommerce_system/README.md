# 🛒 E-Commerce & Order Management System

A Python-based E-Commerce & Order Management System built to practice Object-Oriented Programming (OOP), inventory management, shopping cart operations, payment processing, and order handling.

This project simulates the core workflow of a simple online shopping application using Python classes, services, custom exceptions, and modular programming.

## 📌 Project Overview

The E-Commerce & Order Management System allows customers to browse available products, add items to a shopping cart, calculate totals, place orders, select payment methods, view order details, and cancel eligible orders.

The project focuses on applying Python OOP concepts to a practical, real-world-inspired use case.

## ✨ Features

### 🛍️ Product Management

* Display available products.
* View product IDs, names, prices, and stock quantities.
* Validate product information.
* Prevent invalid prices and negative stock values.

### 🛒 Shopping Cart

* Add products to the cart.
* Update the quantity of existing cart items.
* Remove products from the cart.
* Calculate the total cart amount.
* Display cart contents and subtotals.
* Validate product quantities.

### 📦 Inventory Management

* Check product availability before adding items to the cart.
* Validate stock availability during checkout.
* Reserve stock when an order is placed.
* Restore reserved stock when an eligible order is cancelled or checkout fails.

### 🧾 Order Management

* Create orders with unique order IDs.
* Store customer and order-item information.
* Calculate the total order amount.
* Track order status.
* Retrieve order details.
* Cancel eligible orders.
* Maintain customer order history.

### 💳 Payment Methods

The project includes three simulated payment options:

* UPI Payment
* Card Payment
* Cash on Delivery (COD)

**Note:** These payment methods simulate payment selection and confirmation. They do not connect to real payment gateways or process actual financial transactions.

### 🔔 Notification System

The project demonstrates a notification system with simulated:

* Email notifications
* SMS notifications
* WhatsApp notifications

Notifications are printed to the terminal; no actual messages are sent.

### 🛡️ Error Handling

Custom exceptions are used to handle situations such as:

* Insufficient stock
* Empty shopping cart
* Payment processing failure
* Invalid order status
* Missing products or orders

Input validation and exception handling help prevent common errors from terminating the application unexpectedly.

## 🧠 Python Concepts Used

This project provides practical experience with:

* Classes and Objects
* Constructors (`__init__`)
* Instance Attributes
* Encapsulation
* Properties and Setters
* Inheritance
* Method Overriding
* Polymorphism
* Abstraction using `ABC` and `@abstractmethod`
* Dunder Methods such as `__str__` and `__len__`
* Composition and Object Relationships
* Dependency Injection
* Custom Exceptions
* Exception Handling (`try`, `except`, `raise`)
* Dictionaries and Lists
* Modular Programming
* Separation of Responsibilities

## 📁 Project Structure

```text
ecommerce_system/
│
├── main.py
│
├── models/
│   ├── user.py
│   ├── product.py
│   ├── cart.py
│   ├── order.py
│   └── order_item.py
│
├── services/
│   ├── inventory_service.py
│   ├── order_service.py
│   └── notification_service.py
│
├── payments/
│   ├── base.py
│   ├── upi.py
│   ├── card.py
│   └── cash_on_delivery.py
│
├── notifications/
│   ├── email.py
│   ├── sms.py
│   └── whatsapp.py
│
├── exceptions.py
└── README.md
```

## ⚙️ Requirements

* Python 3.10 or later recommended
* A code editor such as Visual Studio Code
* A terminal or command prompt

No external Python packages are required for the core implementation, provided the project uses only Python's standard library.

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone <YOUR_REPOSITORY_URL>
```

Replace `<YOUR_REPOSITORY_URL>` with your actual GitHub repository URL.

### 2. Open the Project Directory

```bash
cd ecommerce_system
```

### 3. Run the Application

```bash
python main.py
```

On some Windows systems, you may need to use:

```powershell
py main.py
```

## 🖥️ Application Menu

When the application starts, an interactive menu allows the user to:

```text
==================================================
       E-COMMERCE ORDER MANAGEMENT SYSTEM
==================================================
1. View Products
2. Add Product to Cart
3. View Shopping Cart
4. Remove Product from Cart
5. Checkout / Place Order
6. View Order Details
7. Cancel Order
8. View Customer Profile
9. Exit
==================================================
```

Choose an option by entering its corresponding number.

## 🧪 Example Workflow

A typical shopping workflow is:

1. Start the application.
2. View available products.
3. Add a product to the shopping cart.
4. Review the cart and total amount.
5. Proceed to checkout.
6. Sele
