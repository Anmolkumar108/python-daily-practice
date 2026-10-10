class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name 
        self.price = price

    def display_product(self):
        return {
            "Product_Id": self.product_id,
            "Name": self.name,
            "Price": self.price
        }
class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def calculate_subtotal(self):
        return self.product.price * self.quantity

    def display_CartItem(self):
        return {
            "Product Name": self.product.name,
            "Price": self.product.price,
            "Quantity": self.quantity,
            "Total_Cost": self.calculate_subtotal()
        }
class ShoppingCart:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []

    def add_item(self, cart_item):
        self.items.append(cart_item)

    def remove_item(self, product_id):
        for cart_item in self.items:
            if cart_item.product.product_id == product_id:
                self.items.remove(cart_item)
                print(f"{cart_item.product.name} removed from cart.")
                return

        print(f"Product ID {product_id} not found in cart.")

    def display_cart(self):
        if not self.items:
            print(f"{self.customer_name}'s cart is empty.")
            return

        print(f"Shopping cart for {self.customer_name}:")
        print(f"{'Product':<15} {'Price':>12} {'Quantity':>10} {'Subtotal':>15}")
        for cart_item in self.items:
            product = cart_item.product
            subtotal = cart_item.calculate_subtotal()
            print(
                f"{product.name:<15} ₹{product.price:>10,} "
                f"{cart_item.quantity:>10} ₹{subtotal:>13,}"
            )

    def calculate_total(self):
        return sum(cart_item.calculate_subtotal() for cart_item in self.items)


if __name__ == "__main__":
    import sys

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    laptop = Product(1, "Laptop", 50000)
    mouse = Product(2, "Mouse", 500)
    keyboard = Product(3, "Keyboard", 1500)

    cart = ShoppingCart("Anmol")
    cart.add_item(CartItem(laptop, 1))
    cart.add_item(CartItem(mouse, 2))
    cart.add_item(CartItem(keyboard, 1))

    cart.display_cart()
    print(f"\nTotal bill: ₹{cart.calculate_total():,}")
        