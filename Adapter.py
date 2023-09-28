# Ορίζουμε την κλάση που αναμένει η `PaymentProcessor`
class PaymentProvider:
    def process_payment(self, amount):
        pass


# Ορίζουμε την κλάση του εξωτερικού πάροχου πληρωμών
class ExternalPaymentProvider:
    def make_payment(self, amount):
        print(f"Processing payment of {amount} via external payment provider")


# Ορίζουμε τον Adapter
class ExternalPaymentProviderAdapter(PaymentProvider):
    def __init__(self, external_payment_provider):
        self.external_payment_provider = external_payment_provider

    def process_payment(self, amount):
        self.external_payment_provider.make_payment(amount)


# Ορίζουμε την κλάση PaymentProcessor
class PaymentProcessor:
    def process_payment(self, payment_provider, amount):
        payment_provider.process_payment(amount)


# Κύριο πρόγραμμα
def main():
    external_provider = ExternalPaymentProvider()
    adapter = ExternalPaymentProviderAdapter(external_provider)

    payment_processor = PaymentProcessor()
    payment_processor.process_payment(adapter, 100)


if __name__ == '__main__':
    main()
