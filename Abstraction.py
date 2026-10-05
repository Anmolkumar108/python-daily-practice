from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self):
         print(f"Amount: {self.amount}")

class payment(Payment):
     def __init__(self, amount):
          self.amount = amount
     def pay(self):
          print(f"Amount: {self.amount}")

class UPI(Payment):
     def __init__ (self,upi_id):
          self.upi_id = upi_id
     def pay(self):
         print(f"UPI_I'D: {self.upi_id}")
class Card(Payment):
     def __init__(self,card_number):
          self.card_number = card_number
     def pay(self):
          print(f"Card Number: {self.card_number}")
class Cash(Payment):
     def pay(self):
          print("----- SucessFull Cash Withdrawal ----- ")

amount = payment(1000)
upi = UPI("akanmol@45")
card = Card(5655555)
cash = Cash()

amount .pay()
upi.pay()
card.pay()
cash.pay()



from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, amount):
        self.amount = amount  # Jo amount bahar se aayega wo yahan set ho jayega

    @abstractmethod
    def pay(self):
        pass

    @abstractmethod
    def take_input(self):
        pass

class UPI(Payment):
    def __init__(self, amount):
        super().__init__(amount)
        self.upi_id = ""

    def take_input(self):
        # Yahan amount nahi mangenge, sirf UPI ID mangenge
        self.upi_id = input("Enter the UPI ID: ")

    def pay(self):
        print(f"Amount: {self.amount}")
        print(f"UPI ID: {self.upi_id}")

class Card(Payment):
    def __init__(self, amount):
        super().__init__(amount)
        self.Card_Number = ""
        
    def take_input(self):
        # Yahan sirf Card Number mangenge
        self.Card_Number = input("Enter the Card Number: ")

    def pay(self):
        print(f"Amount: {self.amount}")
        print(f"Card Number: {self.Card_Number}")

class Cash(Payment):
    def __init__(self, amount):
        super().__init__(amount)
        
    def take_input(self):
        # Cash mein koi extra detail nahi chahiye, toh ise pass kar denge
        pass 
        
    def pay(self):
        print(f"Paid {self.amount} Using Cash")


# =======================================
# ==== EXECUTION FLOW (MAIN CODE) ====
# =======================================

# 1. Sabse pehle AMOUNT ek hi baar input le lo
common_amount = int(input("Enter the Amount for all payments: "))

# 2. Ab wahi same amount sabhi objects mein pass kar do
print("\n--- Enter UPI Details ---")
upi = UPI(common_amount)
upi.take_input()

print("\n--- Enter Card Details ---")
card = Card(common_amount)
card.take_input()

cash = Cash(common_amount)
# cash.take_input() bulane ki zaroorat nahi kyunki usme koi extra details nahi chahiye

# 3. Final Payment Details Print karna
print("\n=======================================")
print("========= Payment Details =========")
print("=======================================")

upi.pay()
print("----------------")
card.pay()
print("----------------")
cash.pay()

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
