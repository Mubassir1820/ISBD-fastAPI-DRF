# Encapsulation

class BankAccount():
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            
    def withdraw(self, amount):
        if 0 < amount < self.__balance:
            self.__balance -= amount
            
    def get_balance(self):
        return self.__balance
        
account1 = BankAccount('123456', 1000)
account1.deposit(1000)
account1.withdraw(500)
print(account1.get_balance())


# Inheritance

class Car():
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print("Engine Started")

class SportsCar(Car):
    def __init__(self, make, model, turbo):
        super().__init__(make, model)
        self.turbo = turbo

    def activate_turbo(self):
        print("Turbo activated")

ferrari = SportsCar("Ferrari", '911', True)
ferrari.activate_turbo()
ferrari.start_engine()


# Abstraction
 
from abc import ABC, abstractmethod
class Notification(ABC):
    @abstractmethod
    def format_message(self, message):
        """Format the message for specific notification type"""
        pass

    @abstractmethod
    def send(self, message):
        """Send the formatted message"""
        pass

class EmailNotification(Notification):
    def format_message(self, message):
        return f"Subject: Notification\n\n {message}"
    
    def send(self, message):
        formatted_message = self.format_message(message)
        print(f"Sending Email: {formatted_message}")

class SMSNotification(Notification):
    def format_message(self, message):
        return f"SMS: {message}"
    def send(self, message):
        formatted_message = self.format_message(message)
        print(f"Sending SMS: {formatted_message}")

def notify_user(notification: Notification, message):
    notification.send(message)

email_notification = EmailNotification()
sms_notification = SMSNotification()

notify_user(email_notification, "You have a new Email")
notify_user(sms_notification, "You have a new Sms")