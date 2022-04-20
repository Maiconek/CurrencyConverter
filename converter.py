from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://free.currconv.com"
API_KEY = #enter your api key here

printer = PrettyPrinter()

def get_currencies():
    endpoint = f"/api/v7/currencies?apiKey={API_KEY}"
    link = BASE_URL + endpoint
    data = get(link).json()['results']
    
    data = list(data.items())
    data.sort()
    
    return data
    
def print_currencies(currencies):
    counter = 0
    for name, currency in currencies:
        name = currency['currencyName']
        _id = currency['id']
        symbol = currency.get("currencySymbol", "")
        counter = counter + 1
        print(f"{counter}. {_id} {name} {symbol}")

def exchange_rate(currency1, currency2):
    endpoint = f"/api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()

    if len(data) == 0:
        print("Invalid currencies")
        return

    rate = list(data.values())[0]
    print(f"{currency1} -> {currency2} = {rate}")

    return rate

def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)
    
    if rate == None:
        return
    
    try:
        amount = float(amount)
    except:
        print('Invalid amount.')
        return

    converted_amount = rate * amount
    converted_amount = format(converted_amount, '0.2f')
    print(f"{amount} in {currency1} is equal to {converted_amount} in {currency2}")
    return converted_amount

def main():
    currencies = get_currencies()
    print("Welcome to currencies converter")
    print("List - lists the diffrent currencies")
    print("Convert - from one currency to another")
    print("Rate - get the exchange rate of two currencies")
    print()

    while True:
        command = input("Enter a command (q to quit): ").lower()

        if command == "q":
            break
        elif command == "list":
            print(print_currencies(currencies))
        elif command == "convert":
            currency1 = input("Enter a basecurrency (id): ").upper()
            amount = input(f"Enter an amount of {currency1}: ")
            currency2 = input("Enter a currency to convert (id) to : ").upper()
            convert(currency1, currency2, amount)
        elif command == "rate":
            currency1 = input("Enter a basecurrency (id): ").upper()
            currency2 = input("Enter a currency to convert (id) to : ").upper()
            exchange_rate(currency1, currency2)
        else:
            print("Unknown command")

main()


