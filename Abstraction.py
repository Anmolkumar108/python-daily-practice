from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self,amount = 0):
       self.amount = amount
    def get_amount(self):
        self.amount = int(input("Enter the Amount: "))

    @abstractmethod
    def pay(self):
        pass

    @abstractmethod
    def take_input(self):
        pass

class UPI(Payment):
    def __init__(self, amount = 0, upi_id=""):
        super().__init__(amount)
        self.upi_id = upi_id

    def pay(self):
        print(f"Amount: {self.amount}")
        print(f"UPI ID : {self.upi_id}")

    def take_input(self):
        self.get_amount()
        self.upi_id = input("Enter the UPI ID: ")

class Card(Payment):
    def __init__(self, amount = 0 ,Card_Number = ""):
        super().__init__(amount)
        self.Card_Number = Card_Number

    def pay(self):
        print(f"Amount: {self.amount}")
        print(f"Card Number: {self.Card_Number}")

    def take_input(self):
        self.get_amount()
        self.Card_Number = input("Enter the Card Number: ")

class Cash(Payment):
    def __init__(self, amount=0):
        super().__init__(amount)
        
    def take_input(self):
        self.get_amount() 
        
    def pay(self):
        print(f"Paid {self.amount} Using Cash")

# === Corrected Execution Flow ===

print("--- Enter UPI Details ---")
upi = UPI()
upi.take_input()

print("\n--- Enter Card Details ---")
card = Card()
card.take_input()

print("\n--- Enter Cash Details ---")
cash = Cash()
cash.take_input()

print("\n=======================================")
print("========= Payment Details =========")
print("=======================================")

upi.pay()
print("----------------")
card.pay()
print("----------------")
cash.pay()
