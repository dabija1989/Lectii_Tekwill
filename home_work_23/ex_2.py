"""
Dacă aruncați o privire în fișierul conversion_rates.json, veți vedea o listă foarte lungă cu toate monedele și rata de
 conversie a acestora din și în MDL.
Sarcină

Creați un program care va încărca această listă în program.

La pornirea programului, afișați lista tuturor conversiilor posibile, cu ratele de la cea mai mică la cea mai mare.

Permiteți utilizatorului să introducă numele monedei către care să se facă conversia. Exemplu: EUR sau MDL.

    Dacă moneda introdusă este MDL, atunci cereți utilizatorului să introducă din nou moneda către care să se
    facă conversia din MDL. Exemplu: USD
        Permiteți utilizatorului să introducă valoarea MDL pentru a o converti în moneda respectivă.
        Afișați valoarea convertită cu doar 2 zecimale (de exemplu, 92.43)
    Dacă moneda introdusă nu este MDL, atunci:
        Permiteți utilizatorului să introducă valoarea MDL pentru a o converti în moneda respectivă.

Condiții

    Întregul program ar trebui să fie orientat pe obiecte (să utilizeze doar clase), cu excepția fișierului main.py
    care va rula programul.
    Ar trebui să creați un obiect CurrencyConversion, care va stoca toate informațiile despre fiecare conversie.
Exemplu. CurrencyConversion(from="MDL", to="EUR", rate=0.049175765442905, inverse_rate=20.335219818002, name=" EUR")
    Pentru a avea posibilitatea de a sorta obiectele CurrencyConversion, implementați funcțiile __lt__, __eq__.
    Aceste funcții ar trebui să compare ratele obiectelor CurrencyConversion.
    Aveți un serviciu CurrencyConversionService care va gestiona toate informațiile despre conversiile de valută și
    ar trebui să aibă cel puțin următoarea metodă.
        convert(from_currency, to_currency, amount)

Considerații

Json-ul conține un dicționar de dicționare. Nu este o listă, așa că acordați atenție și analizați datele cu care
lucrați înainte de a începe.
"""

import json
from urllib.request import urlopen


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


class CurrencyConversionService:
    def __init__(self, conversion_rates):
        self.conversions = []
        for currency, data in conversion_rates.items():
            self.conversions.append(CurrencyConversion(
                from_currency='MDL',  # Assuming conversions are always from MDL
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
        return None  # Return None if conversion is not found


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
