from abc import ABC, abstractmethod

class NotificationStrategy(ABC):
    @abstractmethod
    def send(self, user, message):
        pass

class EmailNotificationStrategy(NotificationStrategy):
    def send(self, user, message):
        print(f"Sending email to {user.email}: {message}")

class SMSNotificationStrategy(NotificationStrategy):
    def send(self, user, message):
        print(f"Sending SMS to {user.phone_number}: {message}")

class PushNotificationStrategy(NotificationStrategy):
    def send(self, user, message):
        print(f"Sending push notification to {user.device_id}: {message}")

class NotificationManager:
    def __init__(self):
        self._strategies = {}

    def register_strategy(self, notification_type, strategy):
        self._strategies[notification_type] = strategy

    def send_notification(self, user, notification_type, message):
        strategy = self._strategies.get(notification_type)
        if strategy:
            strategy.send(user, message)
        else:
            raise ValueError(f"No strategy registered for type {notification_type}")


class User:
    def __init__(self, email, phone_number, device_id):
        self.email = email
        self.phone_number = phone_number
        self.device_id = device_id

if __name__ == "__main__":
    # Create users
    user1 = User(email="user1@example.com", phone_number="1234567890", device_id="device123")

    # Create notification strategies
    email_strategy = EmailNotificationStrategy()
    sms_strategy = SMSNotificationStrategy()
    push_strategy = PushNotificationStrategy()

    # Create and configure notification manager
    manager = NotificationManager()
    manager.register_strategy("email", email_strategy)
    manager.register_strategy("sms", sms_strategy)
    manager.register_strategy("push", push_strategy)

    # Send notifications
    manager.send_notification(user1, "email", "Hello via Email!")
    manager.send_notification(user1, "sms", "Hello via SMS!")
    manager.send_notification(user1, "push", "Hello via Push Notification!")
