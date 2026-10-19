class OrderItem:
    def __init__(self, product, quantity: int):
        self._product = product

        if isinstance(quantity, bool) or not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        self._quantity = quantity

        self._price = product.price

    @property
    def product (self):
        return self._product
    @property
    def quantity(self) -> int:
        return self._quantity
    @property
    def price(self) -> float:
        return self._price
    @property
    def subtotal(self) -> float:
        return self._price * self._quantity

    def __str__(self):
         return (f"Product: {self._product.name} | "
                f"Price (at order time): ₹{self._price} | "
                f"Quantity: {self._quantity} | "
                f"Subtotal: {self.subtotal}")
