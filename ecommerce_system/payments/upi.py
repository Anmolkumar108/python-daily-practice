from payments.base import PaymentMethod

class UPIPayment(PaymentMethod):
    def pay(self, amount):
        print(f"[UPI Payment]: Successfully paid ₹{amount} using UPI.")