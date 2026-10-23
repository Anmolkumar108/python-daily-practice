import sys

sys.stdout.reconfigure(encoding="utf-8")

from models.user import User, Customer, Admin
from models.product import Product
from models.order_item import OrderItem
from models.cart import ShoppingCart

# ==========================================
# 1. USER, CUSTOMER AND ADMIN TESTING
# ==========================================

print("\n========== USER TESTING ==========")

user = User("U101", "Anmol Singh", "anmol@example.com")
print(user)

print("\n========== CUSTOMER TESTING ==========")

customer = Customer("C101", "Rahul Kumar", "rahul@example.com", None)
print(customer)

customer.add_order("ORD101")
customer.add_order("ORD102")

print("\nCustomer After Adding Orders:")
print(customer)

print("\n========== ADMIN TESTING ==========")

admin = Admin("A101", "Anmol Singh", "admin@example.com")
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

# Naya product banate hain taaki stock update ke test ka OrderItem par koi effect na pade.
product_item = Product("P102", "Wireless Mouse", 799, 25)

item = OrderItem(product_item, 2)

print(item)

print("\n--- Updating Original Product Price ---")

product_item.price = 999

print(f"Current Product Price: ₹{product_item.price}")

print("\nOrder Item After Product Price Update:")
print(item)

# ==========================================
# 4. CART ITEM TESTING
# ==========================================

def test_shopping_cart():
    print("\n=== ShoppingCart Testing Start ===")
    
    # 1. Sample Products create karna (stock ke saath)
    p1 = Product(product_id="P001", name="Wireless Mouse", price=499, stock=50)
    p2 = Product(product_id="P002", name="Mechanical Keyboard", price=2499, stock=20)
    
    # 2. Cart initialize karna
    cart = ShoppingCart()
    print(f"Initial Cart State: {cart}")
    print(f"Initial Length: {len(cart)}\n")
    
    # 3. Items add karna
    print("--- Adding Items ---")
    cart.add_item(p1, 2)  # 2 Mouse
    cart.add_item(p2, 1)  # 1 Keyboard
    print(cart)
    print(f"Total Items Count: {len(cart)}")
    print(f"Total Amount: ₹{cart.get_total()}\n")
    
    # Same product dobara add karne par quantity update check karna
    print("--- Updating Quantity for Existing Item (Mouse +1) ---")
    cart.add_item(p1, 1)
    print(cart)
    print(f"Updated Total Amount: ₹{cart.get_total()}\n")
    
    # 4. Item remove karna (Valid ID)
    print("--- Removing Item (P001 - Mouse) ---")
    cart.remove_item("P001")
    print(cart)
    print(f"Length after removal: {len(cart)}\n")
    
    # Error Handling check (Invalid/Non-existent Product ID)
    print("--- Testing Error Handling for Invalid Product ID ---")
    try:
        cart.remove_item("P999")
    except ValueError as e:
        print(f"Captured Expected Error: {e}\n")
        
    # 6. Clear cart check
    print("--- Clearing Cart ---")
    cart.clear()
    print(cart)
    print(f"Length after clear: {len(cart)}")
    print("\n=== Testing Completed Successfully! ===")

if __name__ == "__main__":
    test_shopping_cart()