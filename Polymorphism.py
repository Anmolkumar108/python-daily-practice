# class Dog:
#     def sound(self):
#         print("Dog barks")


# class Cat:
#     def sound(self):
#         print("Cat meows")


# class Cow:
#     def sound(self):
#         print("Cow moos")

# animals = [Dog(), Cat(), Cow()]

# for animal in animals:
#     animal.sound()


# # def start_vehicle(vehicle):
# #     vehicle.move()
# # class Car:
# #      def move(self):
# #           print("Car is moving")
# # class Bike:
# #      def move(self):
# #           print("Bike is moving")
# # class Bus:
# #      def  move(Self):
# #           print("Bus is moving")
# # car = Car()
# # bike = Bike()
# # bus = Bus()

# # start_vehicle(car)
# # start_vehicle(bike)
# # start_vehicle(bus)


# numbers = [10, 20, 30, 40, 50]

# name = "Anmol"

# student = {
#     "name": "Anmol",
#     "course": "BCA",
#     "college": "SIT"
# }

# int_add = 10 + 20
# int_string = "10" + "20"
# int_list = [1 , 2] + [3 , 4]

# print(len(numbers))
# print(len(name))
# print(len(student))
# print(int_add)
# print(int_string)
# print(int_list)



# class Payment():
#     def pay(Self):
#         print("Processing payment")
# class Upi(Payment):
#     def pay(self):
#         print("Paid using UPI")
# class Card(Payment):
#     def pay(self):
#         print("Paid using Card")
# class Cash(Payment):
#     def pay(Self):
#         print("Paid using Cash")

# Payment = [Upi(), Card(), Cash()]

# for customer in Payment:
#     customer.pay()



def notify(notification, message): 
    notification.send(message) 

class EmailNotification: 
    def send(self, message):
        print(f"Email sent: {message}") 

class SMSNotification: 
    def send(self, message): 
        print(f"SMS sent: {message}") 

class WhatsAppNotification: 
    def send(self, message): 
        print(f"WhatsApp message sent: {message}") 

emailNotification = EmailNotification() 
smsnotification = SMSNotification() 
whatsAppNotification = WhatsAppNotification() 

msg = "Hello Anmol"

notify(emailNotification, msg) 
notify(smsnotification, msg) 
notify(whatsAppNotification, msg)
