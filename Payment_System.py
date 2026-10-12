class PaymentMethod:
    def pay(self, amount):
        print(f"Payment amount: ₹{amount}")

class UPIPayment(PaymentMethod):
    def pay(self, amount):
        print(f"UPI payment of ₹{amount} successful.")

class PaymentProcessor:
    def __init__(self, payment_method):
        self.payment_method = payment_method

    def process_payment(self, amount):
        self.payment_method.pay(amount)


upi_payment = UPIPayment()
payment_processor = PaymentProcessor(upi_payment)
payment_processor.process_payment(500)

