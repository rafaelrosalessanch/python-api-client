import requests

URL = "https://api.coindesk.com/v1/bpi/currentprice.json"

def get_bitcoin_price():
    response = requests.get(URL)
    data = response.json()
    price = data["bpi"]["USD"]["rate"]
    return price

if __name__ == "__main__":
    price = get_bitcoin_price()
    print(f"Bitcoin price (USD): {price}")