from payments.base import PaymentMethod

class CardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"[Card Payment]: Successfully paid ₹{amount} using Card.")