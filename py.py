class Logger:
    def __init__(self):
        self.logs = []

    def log(self, user, amount, result):
        log_entry = {
            'user': user,
            'amount': amount,
            'result': result
        }
        self.logs.append(log_entry)
        # For demonstration, print the log entry
        print(f"Logged: User={user}, Amount={amount}, Converted Result={result}")

    def get_logs(self):
        return self.logs


class CurrencyConverter:
    # Class attribute to store exchange rates
    exchange_rates = {
        'USD': 1.0,
        'EUR': 0.85,
        'JPY': 110.0,
        'GBP': 0.75
        # Add more currencies as needed
    }

    def __init__(self, amount, from_currency, to_currency, logger):
        self.amount = amount
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.logger = logger

        # Validate currencies upon initialization
        if not self.is_valid_currency(from_currency):
            raise ValueError(f"Invalid from_currency code: {from_currency}")
        if not self.is_valid_currency(to_currency):
            raise ValueError(f"Invalid to_currency code: {to_currency}")

    def convert(self):
        # Check if exchange rates are available for the currencies
        if (self.from_currency not in self.exchange_rates or
                self.to_currency not in self.exchange_rates):
            raise ValueError("Exchange rate not available for given currencies.")

        # Convert amount to base currency (assumed USD here)
        amount_in_base = self.amount / self.exchange_rates[self.from_currency]
        # Convert from base to target currency
        result = amount_in_base * self.exchange_rates[self.to_currency]

        # Log the conversion
        self.logger.log(user='Unknown', amount=self.amount, result=result)

        return result

    @classmethod
    def update_rate(cls, currency_code, rate):
        if not cls.is_valid_currency(currency_code):
            raise ValueError(f"Invalid currency code: {currency_code}")
        cls.exchange_rates[currency_code] = rate

    @staticmethod
    def is_valid_currency(currency_code):
        # For simplicity, check if the code is 3 uppercase letters
        return isinstance(currency_code, str) and len(currency_code) == 3 and currency_code.isalpha() and currency_code.isupper()

