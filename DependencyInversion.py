from abc import ABC, abstractmethod

class NotificationSenderInterface(ABC):
    @abstractmethod
    def send_notification(self, message):
        pass

class EmailNotificationSender(NotificationSenderInterface):
    def send_notification(self, message):
        print("Sending email notification:", message)

class SMSNotificationSender(NotificationSenderInterface):
    def send_notification(self, message):
        print("Sending SMS notification:", message)

class NotificationManager:
    def __init__(self, sender):
        self.sender = sender

    def send_notification(self, message):
        self.sender.send_notification(message)

# Χρήση του παραδείγματος
email_sender = EmailNotificationSender()
sms_sender = SMSNotificationSender()

notification_manager = NotificationManager(email_sender)
notification_manager.send_notification("Hello, email!")

notification_manager = NotificationManager(sms_sender)
notification_manager.send_notification("Hello, SMS!")
