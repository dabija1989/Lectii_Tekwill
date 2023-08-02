import json
from urllib.request import urlopen
from currency_conversion_service import CurrencyConversionService


def main():
    url = "https://raw.githubusercontent.com/mtricolici98/tekwillLiveV3/master/lesson_23_homework/conversion_rates.json"
    response = urlopen(url)
    conversion_rates = json.loads(response.read().decode())

    currency_service = CurrencyConversionService(conversion_rates)

    print("List of available currencies for conversion:")
    for conversion in currency_service.conversions:
        print(f"{conversion.to_currency}: {conversion.name}")

    from_currency = input("Enter the currency you want to convert from: ").upper()
    to_currency = input("Enter the currency you want to convert to: ").upper()
    amount = float(input("Enter the amount: "))

    converted_amount = currency_service.convert(from_currency, to_currency, amount)

    if converted_amount is not None:
        print(f"Converted amount: {converted_amount:.2f} {to_currency}")
    else:
        print("Currency conversion not available or invalid input.")


if __name__ == "__main__":
    main()
