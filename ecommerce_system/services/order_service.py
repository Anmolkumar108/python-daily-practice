from exceptions import (
    EmptyCartError,
    PaymentFailedError,
    ProductNotFoundError,
    InvalidOrderStatusError,
)
from models.order import Order


class OrderService:
    def __init__(self, inventory_service, notification_manager):
        self._inventory_service = inventory_service
        self._notification_manager = notification_manager
        self._orders = {}

    def checkout(self, customer, cart, payment_method, order_id):
        if not cart.items:
            raise EmptyCartError("Cart is empty. Order cannot be placed.")


        if order_id in self._orders:
            raise ValueError(f"Order ID '{order_id}' already exists.")
        
        total = cart.get_total()


        reserved_items = []

        try:
            for item in cart.items:
                self._inventory_service.check_stock(item.product, item.quantity)
                self._inventory_service.reserve_stock(item.product, item.quantity)
                reserved_items.append(item)

        except Exception:

            for item in reserved_items:
                self._inventory_service.release_stock(item.product, item.quantity)
            raise


        try:
            payment_method.pay(total)

        except Exception as e:

            for item in reserved_items:
                self._inventory_service.release_stock(item.product, item.quantity)

            if isinstance(e, PaymentFailedError):
                raise

            raise PaymentFailedError(
                f"Payment processing failed: {e}"
            ) from e


        try:
            order = Order(order_id, customer, list(cart.items))
            order.status = "Confirmed"

        except Exception:

            for item in reserved_items:
                self._inventory_service.release_stock(item.product, item.quantity)
            raise


        self._orders[order_id] = order


        customer.add_order(order)


        cart.clear()


        try:
            self._notification_manager.send_notification(
                f"Order Success! Order ID: {order_id} "
                f"has been placed successfully. "
                f"Total Amount: ₹{total}"
            )
        except Exception:

            pass

        return order

    def get_order(self, order_id):
        if order_id not in self._orders:
            raise ProductNotFoundError(f"Order ID '{order_id}' not found.")

        return self._orders[order_id]

    def cancel_order(self, order_id):

        order = self.get_order(order_id)

  
        status = getattr(order, "status", "Confirmed")

        if status not in ["Confirmed", "Processing"]:
            raise InvalidOrderStatusError(
                f"Order cannot be cancelled because "
                f"its status is '{status}'."
            )


        for item in order.items:
            self._inventory_service.release_stock(item.product, item.quantity)


        order.status = "Cancelled"

        try:
            self._notification_manager.send_notification(
                f"Order Cancelled: Order ID {order_id} "
                f"has been cancelled and stock has been restored."
            )
        except Exception:
            pass

        return order
