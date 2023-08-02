from currency_conversion import CurrencyConversion


class CurrencyConversionService:
    def __init__(self, conversion_rates):
        self.conversions = []
        for currency, data in conversion_rates.items():
            self.conversions.append(CurrencyConversion(
                from_currency='MDL',
                to_currency=data['code'],
                rate=data['rate'],
                inverse_rate=data['inverseRate'],
                name=data['name']
            ))
        self.conversions.sort()

    def convert(self, from_currency, to_currency, amount):
        if from_currency == 'MDL':
            conversion = next((conv for conv in self.conversions if conv.to_currency == to_currency), None)
            if conversion:
                converted_amount = amount * conversion.rate
                return round(converted_amount, 2)
        else:
            conversion = next((conv for conv in self.conversions if conv.to_currency == from_currency), None)
            if conversion:
                converted_amount = amount * conversion.inverse_rate
                return round(converted_amount, 2)
        return None
