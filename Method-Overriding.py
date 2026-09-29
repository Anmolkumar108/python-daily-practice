# class Animal:
#     def sound(self):
#         print("Animal makes a sound")
# class Dog(Animal):
#     def sound(self):
#         Animal.sound(self)
#         print("Dog barks")

# Dog1 = Dog()
# Dog1.sound()



class Payment:
    def __init__(self , amount):
        self.amount = amount
    def process_payment(self):
        print(f"Processing payment of ₹{self.amount}")
    def input_detail(Self):
        Self.amount = int(input("Enter Amount: "))

class UPIPayment(Payment):
    def __init__(self, amount , upi_id):
        super().__init__(amount)
        self.upi_id = upi_id
    def process_payment(self):
        super().process_payment()
        print(f"Upi_Id: {self.upi_id}")
        print("UPI Payment Successful")

    def input_detail(self):
        self.upi_id = int(input(f"Enter Upi_Id {self.upi_id}"))

class BankPayment(UPIPayment):
    def __init__(self, amount, upi_id, account_number, bank_name):
        super().__init__(amount, upi_id)
        self.account_number = account_number
        self.bank_name = bank_name
    def process_payment(self):
        super().process_payment()
        print(f"Bank:{self.bank_name}")
        print(f"Account Number: {self.account_number}")
        print("Bank Payment Successful")
    def input_detail(self):
           self.bank_name = input(f"Enter Bank Name: {self.bank_name}")
           self.account_number = int(input(f"Enter Account Number : {self.account_number}"))

employ1 = BankPayment(0,0,"",0)
employ1.input_detail()
employ1.process_payment()

