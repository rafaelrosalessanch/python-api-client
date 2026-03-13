import requests

URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

def get_bitcoin_price():
    response = requests.get(URL)
    data = response.json()
    return data["bitcoin"]["usd"]

if __name__ == "__main__":
    price = get_bitcoin_price()
    print(f"Bitcoin price (USD): {price}")