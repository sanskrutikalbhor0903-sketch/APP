from abc import ABC, abstractmethod

# Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        return f"Paid {amount} using Credit Card {self.card_number}"

class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        return f"Paid {amount} using PayPal account {self.email}"

class BitcoinPayment(PaymentStrategy):
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address

    def pay(self, amount):
        return f"Paid {amount} using Bitcoin wallet {self.wallet_address}"

# Context Class
class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def process_payment(self, amount):
        return self.strategy.pay(amount)


# Example usage


def main():
    # Choose Credit Card Payment
    processor = PaymentProcessor(CreditCardPayment("1234-5678-9777"))
    print(processor.process_payment(500))

    # Switch to PayPal Payment
    processor.set_strategy(PayPalPayment("user@abcd.com"))
    print(processor.process_payment(750))

    # Switch to Bitcoin Payment
    processor.set_strategy(BitcoinPayment("1234abcd"))
    print(processor.process_payment(1200))


if __name__ == "__main__":
    main()