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



class Engine:
    def start(self):
        print("Engine Started.")
class Car:
    def __init__(self):
        self.engine = Engine()
    def Start_Car(self):
        self.engine.start()
        print("Car Started.")
my_car = Car()
my_car.Start_Car()


class Engine:
    def start(self):
        print("Engine Started.")
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    def move(self):
        print("Vehicle is moving.")

class Car(Vehicle):
    def __init__(self, brand):
        super().__init__(brand)
        self.engine = Engine()

    def move(self):
        print("Car is moving.")

    def start_car(self):
        self.engine.start()

class Bike(Vehicle):
    def move(self):
        print("Bike Moving.")

my_car = Car("Toyota")
my_car.start_car()
my_car.move()

my_bike = Bike("Yamaha")
my_bike.move()