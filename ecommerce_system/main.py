from python_Daily_Practice_Chalange.ecommerce_system.models.user import User, Customer, Admin
from python_Daily_Practice_Chalange.ecommerce_system.models.product import Product

user = User("U101", "Anmol Singh", "anmol@example.com")
customer = Customer("C101", "Rahul Kumar", "rahul@example.com", None)
admin = Admin("A101", "Anmol Singh", "admin@example.com")

print(user)
print("\n--- CUSTOMER ---")
print(customer)

customer.add_order("ORD101")
customer.add_order("ORD102")

print("\n--- CUSTOMER AFTER ORDERS ---")
print(customer)

print("\n--- ADMIN ---")
print(admin)

# --------- Product ---------
print("==========================")
print("-------- Product ---------")
print("==========================")

product = Product("P101", "Wireless Mouse", 799, 25)

print(product)

print("\nUpdated Price:")
product.price = 899
print(product.price)

print("\nUpdated Stock:")
product.stock = 0
print(product.stock)