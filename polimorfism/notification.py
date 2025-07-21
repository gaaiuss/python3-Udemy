from abc import ABC, abstractmethod


class Notification(ABC):
    def __init__(self, message):
        self.message = message

    @abstractmethod
    def send(self) -> bool: ...


class Email(Notification):
    def send(self):
        print('Email: sending -', self.message)
        return True


class Sms(Notification):
    def send(self):
        print('SMS: sending -', self.message)
        return True


def notify(notification: Notification):
    notification_sent = notification.send()

    if notification_sent:
        print('Notification sent')
    else:
        print('Failed to send notification')


email_notification = Email('Email test message 123')
notify(email_notification)

sms_notification = Sms('Sms test message 123')
notify(sms_notification)
