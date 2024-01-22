import requests



def get_exchange_rate(base_currency, target_currancy):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()['rates'][target_currancy]



def convert_currency(amount, exchange_rate):
    return amount * exchange_rate



if __name__ == '__main__':
    base_currency = input("Enter base currency: ").upper()
    target_currency = input("Enter target currency: ").upper()
    amount = float(input("Enter amount: "))
    exchange_rate = get_exchange_rate(base_currency, target_currency)
    converted_amount = convert_currency(amount, exchange_rate)
    print(f"{amount} {base_currency} is {converted_amount} {target_currency}")



