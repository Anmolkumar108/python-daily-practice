from models.product import Product
from models.cart import ShoppingCart
from models.user import Customer

from services.inventory_service import InventoryService
from services.order_service import OrderService
from services.notification_service import (
    NotificationManager,
    EmailNotification,
    SMSNotification,
    WhatsAppNotification,
)

from payments.upi import UPIPayment
from payments.card import CardPayment
from payments.cash_on_delivery import CashOnDelivery

from exceptions import (
    EmptyCartError,
    InsufficientStockError,
    PaymentFailedError,
    InvalidOrderStatusError,
    ProductNotFoundError,
)


# ==================================================
# INITIALIZE E-COMMERCE SYSTEM
# ==================================================


def initialize_system():
    cart = ShoppingCart()

    customer = Customer(
        user_id=101,
        name="Anmol Singh",
        email="anmol@example.com",
        cart=cart,
    )

    products = {
        "P101": Product("P101", "Laptop", 55000, 10),
        "P102": Product("P102", "Mouse", 800, 25),
        "P103": Product("P103", "Keyboard", 1500, 15),
        "P104": Product("P104", "Headphones", 2000, 20),
        "P105": Product("P105", "Monitor", 12000, 8),
    }

    inventory_service = InventoryService()

    notification_manager = NotificationManager()
    notification_manager.add_service(EmailNotification())
    notification_manager.add_service(SMSNotification())
    notification_manager.add_service(WhatsAppNotification())

    order_service = OrderService(
        inventory_service=inventory_service,
        notification_manager=notification_manager,
    )

    return customer, cart, products, inventory_service, order_service


# ==================================================
# DISPLAY PRODUCTS
# ==================================================


def display_products(products):
    print("\n" + "=" * 65)
    print("                     AVAILABLE PRODUCTS")
    print("=" * 65)
    print(f"{'ID':<10}{'Product Name':<20}{'Price':<15}{'Stock':<10}")
    print("-" * 65)

    for product in products.values():
        print(
            f"{product.product_id:<10}"
            f"{product.name:<20}"
            f"₹{product.price:<14}"
            f"{product.stock:<10}"
        )

    print("=" * 65)


# ==================================================
# ADD PRODUCT TO CART
# ==================================================


def add_product_to_cart(cart, products, inventory_service):
    display_products(products)

    product_id = input("\nEnter Product ID: ").strip().upper()
    product = products.get(product_id)

    if product is None:
        print("\nError: Product not found.")
        return

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("\nQuantity must be greater than zero.")
            return

        quantity_in_cart = sum(
            item.quantity for item in cart.items if item.product.product_id == product_id
        )
        total_quantity = quantity_in_cart + quantity

        inventory_service.check_stock(product, total_quantity)
        cart.add_item(product, quantity)

        print(f"\n{product.name} added to your cart successfully!")

    except InsufficientStockError as error:
        print(f"\nStock Error: {error}")
        print("Please enter a quantity within the available stock.")

    except ValueError as error:
        print(f"\nInput Error: {error}")


# ==================================================
# REMOVE PRODUCT FROM CART
# ==================================================


def remove_product_from_cart(cart):
    if not cart.items:
        print("\nYour shopping cart is empty.")
        return

    print("\n" + str(cart))
    product_id = input("\nEnter Product ID to remove: ").strip().upper()

    try:
        cart.remove_item(product_id)
        print("\nProduct removed from cart successfully.")

    except ValueError as error:
        print(f"\nError: {error}")


# ==================================================
# SELECT PAYMENT METHOD
# ==================================================


def select_payment_method():
    print("\n" + "-" * 35)
    print("SELECT PAYMENT METHOD")
    print("-" * 35)
    print("1. UPI")
    print("2. Card")
    print("3. Cash on Delivery")

    choice = input("Enter your choice (1-3): ").strip()

    payment_methods = {
        "1": UPIPayment,
        "2": CardPayment,
        "3": CashOnDelivery,
    }

    payment_class = payment_methods.get(choice)

    if payment_class is None:
        print("\nInvalid payment option.")
        return None

    return payment_class()


# ==================================================
# CHECKOUT
# ==================================================


def checkout(customer, cart, order_service):
    if not cart.items:
        print("\nYour cart is empty. Add products before checkout.")
        return

    print("\n" + "=" * 45)
    print("                 CHECKOUT")
    print("=" * 45)
    print(cart)

    confirmation = input("\nDo you want to place this order? (y/n): ").strip().lower()

    if confirmation != "y":
        print("\nCheckout cancelled. Your cart is unchanged.")
        return

    payment_method = select_payment_method()

    if payment_method is None:
        return

    order_id = f"ORD{checkout.next_order_id}"

    try:
        order = order_service.checkout(
            customer=customer,
            cart=cart,
            payment_method=payment_method,
            order_id=order_id,
        )

        checkout.next_order_id += 1

        print("\n" + "=" * 45)
        print("       ORDER PLACED SUCCESSFULLY")
        print("=" * 45)
        print(order)

    except EmptyCartError as error:
        print(f"\nCart Error: {error}")

    except InsufficientStockError as error:
        print(f"\nStock Error: {error}")
        print("Your order could not be placed.")

    except PaymentFailedError as error:
        print(f"\nPayment Error: {error}")
        print("Your cart has been retained.")

    except (ValueError, InvalidOrderStatusError) as error:
        print(f"\nOrder Error: {error}")

    except Exception as error:
        print(f"\nUnexpected checkout error: {type(error).__name__}: {error}")


checkout.next_order_id = 1001


# ==================================================
# VIEW ORDER DETAILS
# ==================================================


def view_order_details(order_service):
    order_id = input("\nEnter Order ID: ").strip()

    try:
        order = order_service.get_order(order_id)

        print("\n" + "=" * 45)
        print("              ORDER DETAILS")
        print("=" * 45)
        print(order)

    except ProductNotFoundError as error:
        print(f"\nOrder Error: {error}")

    except Exception as error:
        print(f"\nUnexpected error: {error}")


# ==================================================
# CANCEL ORDER
# ==================================================


def cancel_order(order_service):
    order_id = input("\nEnter Order ID to cancel: ").strip()

    confirmation = input(
        f"Are you sure you want to cancel {order_id}? (y/n): "
    ).strip().lower()

    if confirmation != "y":
        print("\nOrder cancellation aborted.")
        return

    try:
        order = order_service.cancel_order(order_id)

        print("\nOrder cancelled successfully!")
        print(order)

    except ProductNotFoundError as error:
        print(f"\nOrder Error: {error}")

    except InvalidOrderStatusError as error:
        print(f"\nCancellation Error: {error}")

    except Exception as error:
        print(f"\nUnexpected cancellation error: {error}")


# ==================================================
# VIEW CUSTOMER PROFILE
# ==================================================


def view_customer_profile(customer):
    print("\n" + "=" * 45)
    print("             CUSTOMER PROFILE")
    print("=" * 45)
    print(customer)

    if customer.order_history:
        print("\nORDER HISTORY")
        print("-" * 45)

        for order in customer.order_history:
            print(
                f"Order ID: {order.order_id} | "
                f"Total: ₹{order.total_amount} | "
                f"Status: {order.status}"
            )
    else:
        print("\nNo orders placed yet.")


# ==================================================
# MAIN MENU
# ==================================================


def main():
    customer, cart, products, inventory_service, order_service = initialize_system()

    while True:
        print("\n")
        print("=" * 50)
        print("       E-COMMERCE ORDER MANAGEMENT SYSTEM")
        print("=" * 50)
        print("1. View Products")
        print("2. Add Product to Cart")
        print("3. View Shopping Cart")
        print("4. Remove Product from Cart")
        print("5. Checkout / Place Order")
        print("6. View Order Details")
        print("7. Cancel Order")
        print("8. View Customer Profile")
        print("9. Exit")
        print("=" * 50)

        choice = input("Enter your choice (1-9): ").strip()

        if choice == "1":
            display_products(products)

        elif choice == "2":
            add_product_to_cart(cart, products, inventory_service)

        elif choice == "3":
            print("\n" + str(cart))

        elif choice == "4":
            remove_product_from_cart(cart)

        elif choice == "5":
            checkout(customer, cart, order_service)

        elif choice == "6":
            view_order_details(order_service)

        elif choice == "7":
            cancel_order(order_service)

        elif choice == "8":
            view_customer_profile(customer)

        elif choice == "9":
            print("\nThank you for using our E-Commerce System!")
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 9.")


# ==================================================
# APPLICATION ENTRY POINT
# ==================================================


if __name__ == "__main__":
    main()
