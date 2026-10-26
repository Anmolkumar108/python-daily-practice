from payments.base import PaymentMethod

class CashOnDelivery(PaymentMethod):
    def pay(self, amount):
        print(f"[Cash Payment]: Cash on Delivery selected ₹{amount} using Cash.")