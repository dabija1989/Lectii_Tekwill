class CurrencyConversion:
    def __init__(self, from_currency, to_currency, rate, inverse_rate, name):
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.rate = rate
        self.inverse_rate = inverse_rate
        self.name = name

    def __lt__(self, other):
        return self.rate < other.rate

    def __eq__(self, other):
        return self.rate == other.rate
