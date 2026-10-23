class OrderItem:
    def __init__(self, product, quantity):
        self._product = product

        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity ek positive integer honi chahiye.")
        self._quantity = quantity
        self._price = product.price

    @property
    def product(self):
        return self._product
    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Quantity ek positive integer honi chahiye.")
        self._quantity = value

    @property
    def price(self):
        return self._price

    @property
    def subtotal(self):
        return self._price * self.quantity

    @property
    def get_subtotal(self):
        return self.subtotal

    def __str__(self):
        return f"{self._product.name} (Qty: {self._quantity}) - Unit Price: ₹{self._price} | Subtotal: ₹{self.subtotal}"