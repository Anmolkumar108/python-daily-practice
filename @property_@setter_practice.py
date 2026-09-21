class BankAccount:
    def __init__(self, name, balance):
        self.__name = name         
        self.__balance = balance  
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, value):
         self.__balance = value


BankAccount1 = BankAccount("Anmol Singh", 60000)

print(BankAccount1.name)     
print(BankAccount1.balance)  
print()

BankAccount1.name = "Vicky Singh"
BankAccount1.balance = 1000000

print(BankAccount1.name)     
print(BankAccount1.balance)  