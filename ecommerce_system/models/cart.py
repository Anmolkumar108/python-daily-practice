from models.order_item import OrderItem

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        for item in self.items:
            if item.product.product_id == product.product_id:
                item.quantity += quantity
                return
        order_item = OrderItem(product, quantity)
        self.items.append(order_item)

    def remove_item(self, product_id):
        for i, item in enumerate(self.items):
            if item.product.product_id == product_id:
                del self.items[i]
                return
        raise ValueError(f"Product with ID {product_id} cart mein nahi mila.")

    def get_total(self):
        return sum(item.subtotal for item in self.items)

    def clear(self):
        self.items.clear()

    def __len__(self):
        return len(self.items)

    def __str__(self):
        if not self.items:
            return "ShoppingCart is empty."
        
        lines = [f"Cart Items:"]
        for item in self.items:
            lines.append(f"- {item.product.name} x {item.quantity} = ₹{item.subtotal}")
        
        lines.append(f"Total Amount: ₹{self.get_total()}")
        return "\n".join(lines)