from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

class EmailNotification(NotificationService):
    def send(self, message: str):
        print(f"Email: {message}")

class SMSNotification(NotificationService):
    def send(self, message: str):
        print(f"SMS: {message}")

class NotificationManager:
    def __init__(self, services: list[NotificationService]):
        self.services = services

    def notify(self, message: str):
        for service in self.services:          
            service.send(message)

# --- Main Program Execution --   
email = EmailNotification()
sms = SMSNotification()
   
notification_list = [email, sms]
manager = NotificationManager(notification_list)

manager.notify("Important Update: Your schedule has been updated.")