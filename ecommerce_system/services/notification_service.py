from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotification(NotificationService):
    def send(self, message):
       print(f"[Email Sent]: {message}")

class SMSNotification(NotificationService):
    def send(self, message):
        print(f"[SMS Sent]: {message}")

class WhatsAppNotification(NotificationService):
    def send(self, message):
       print(f"[WhatsApp Sent]: {message}")

class NotificationManager:
    def __init__(self):
        self._services = []

    def add_service(self, service: NotificationService):
        self._services.append(service)

    def send_notification(self, message):
        for service in self._services:
            service.send(message)