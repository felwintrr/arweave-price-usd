import requests


def transaction_cost_in_winston(bytes):
    response = requests.get(f"https://arweave.net/price/{bytes}/")
    return response.text


def winston_to_ar(winston_price):
    return winston_price * (10 ** -12)


def ar_to_usd(ar_price):
    response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=arweave&vs_currencies=usd")

    price = response.json()
    usd_price = price["arweave"]["usd"]

    return ar_price * usd_price

