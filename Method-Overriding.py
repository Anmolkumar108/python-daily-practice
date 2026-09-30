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
    def __init__(self, amount):
        self.amount = amount
        
    def process_payment(self):
        print(f"Processing payment of ₹{self.amount}") 
        
    def input_detail(self):
        self.amount = int(input("Enter Amount: ")) 

class UPIPayment(Payment):
    def __init__(self, amount, upi_id):
        super().__init__(amount)
        self.upi_id = upi_id
        
    def process_payment(self):
        super().process_payment()
        print(f"UPI ID: {self.upi_id}")
        print("UPI Payment Successful")
        
    def input_detail(self):
        super().input_detail() 
        self.upi_id = input("Enter UPI ID: ") 

class BankPayment(UPIPayment):
    def __init__(self, amount, upi_id, account_number, bank_name):
        super().__init__(amount, upi_id)
        self.account_number = account_number
        self.bank_name = bank_name
        
    def process_payment(self):
        super().process_payment()
        print(f"Bank: {self.bank_name}")
        print(f"Account Number: {self.account_number}")
        print("Bank Payment Successful")
        
    def input_detail(self):
        super().input_detail() 
        self.bank_name = input("Enter Bank Name: ")
        self.account_number = int(input("Enter Account Number: "))

employ1 = BankPayment(0, "", 0, "")
employ1.input_detail()

print("=========================")
print("---- Costomer Detaile ----")
print("=========================")
employ1.process_payment()
