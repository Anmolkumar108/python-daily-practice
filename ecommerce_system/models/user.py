class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def __str__(self):
        return (
            f"User Id: {self.user_id}\n"
            f"Name: {self.name}\n"
            f"Email: {self.email}"
        )


class Customer(User):
    def __init__(self, user_id, name, email, cart):
        super().__init__(user_id, name, email)
        self.cart = cart
        self.order_history = []

    def add_order(self, order):
        self.order_history.append(order)

    def __str__(self):
        return (
            f"{super().__str__()}\n"
            f"Cart: {self.cart}\n"
            f"Orders Count: {len(self.order_history)}"
        )


class Admin(User):
    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)
        self.role = "Admin"

    def __str__(self):
        user_str = super().__str__().replace("User Id", "Admin ID")
        return (
            f"{user_str}\n"
            f"Role: {self.role}"
        )