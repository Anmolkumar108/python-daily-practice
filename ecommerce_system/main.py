from models.user import User, Customer, Admin
from models.product import Product
from models.order import OrderItem

# ==========================================

# 1. USER, CUSTOMER AND ADMIN TESTING

# ==========================================

print("\n========== USER TESTING ==========")

user = User("U101", "Anmol Singh", "[anmol@example.com](mailto:anmol@example.com)")
print(user)

print("\n========== CUSTOMER TESTING ==========")

customer = Customer("C101", "Rahul Kumar", "[rahul@example.com](mailto:rahul@example.com)", None)
print(customer)

customer.add_order("ORD101")
customer.add_order("ORD102")

print("\nCustomer After Adding Orders:")
print(customer)

print("\n========== ADMIN TESTING ==========")

admin = Admin("A101", "Anmol Singh", "[admin@example.com](mailto:admin@example.com)")
print(admin)

# ==========================================

# 2. PRODUCT TESTING

# ==========================================

print("\n========== PRODUCT TESTING ==========")

product = Product("P101", "Wireless Mouse", 799, 25)
print(product)

print("\n--- Updating Product Price ---")

product.price = 899
print(f"Updated Price: ₹{product.price}")

print("\n--- Updating Product Stock ---")

product.stock = 0
print(f"Updated Stock: {product.stock}")

# ==========================================

# 3. ORDER ITEM TESTING

# ==========================================

print("\n========== ORDER ITEM TESTING ==========")

# Naya product banate hain taaki stock update

# ke test ka OrderItem par koi effect na pade.

product = Product("P102", "Wireless Mouse", 799, 25)

item = OrderItem(product, 2)

print(item)

print("\n--- Updating Original Product Price ---")

product.price = 999

print(f"Current Product Price: ₹{product.price}")

print("\nOrder Item After Product Price Update:")
print(item)
