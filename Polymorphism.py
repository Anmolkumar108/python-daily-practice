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
