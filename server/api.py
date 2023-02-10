import calculations

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/get-usd-price/{bytes}")
def get_usd_price(bytes: int):
    transaction_cost = calculations.transaction_cost_in_winston(bytes)
    ar_cost = calculations.winston_to_ar(int(transaction_cost))

    return round(calculations.ar_to_usd(ar_cost), 2)
