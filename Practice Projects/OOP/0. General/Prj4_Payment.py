# Practice abstraction & polymorphism

from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def process_payment(self, amount):
        pass


class CardPayment(Payment):
    def process_payment(self, amount):
        return f"Paid {amount}$ using card"

class PayPalPayment(Payment):
    def process_payment(self, amount):
        return f"Paid {amount}$ using PayPal"

card = CardPayment()
paypal = PayPalPayment()

print(card.process_payment(100)) # Paid 100$ using card
print(paypal.process_payment(100)) # Paid 100$ using PayPal