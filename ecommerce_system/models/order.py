class Order:
    def __init__(self, order_id, customer, items):
        if not order_id or not str(order_id).strip():
            raise ValueError("Order ID empty nahi honi chahiye.")

        self._order_id = order_id
        self._customer = customer
        self._items = list(items)
        self._status = "Pending"

    @property
    def order_id(self):
        return self._order_id

    @property
    def customer(self):
        return self._customer

    @property
    def items(self):
        return list(self._items)

    @property
    def total_amount(self):
        return sum(item.subtotal for item in self._items)

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        valid_statuses = [
            "Pending",
            "Confirmed",
            "Processing",
            "Shipped",
            "Delivered",
            "Cancelled",
        ]

        if value not in valid_statuses:
            raise ValueError(f"Invalid order status: {value}")

        self._status = value

    def __str__(self):
        items_details = "\n".join(
            f"  - {item.product.name} x {item.quantity} = ₹{item.subtotal}"
            for item in self._items
        )

        return (
            f"Order ID: {self._order_id}\n"
            f"Customer: {self._customer.name}\n"
            f"Items:\n{items_details}\n"
            f"Total Amount: ₹{self.total_amount}\n"
            f"Status: {self._status}"
        )
