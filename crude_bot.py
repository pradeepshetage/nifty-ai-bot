import os
import time
import pandas as pd
import upstox_client
from datetime import datetime

FILE_NAME = "prices.csv"

configuration = upstox_client.Configuration()
configuration.access_token = os.getenv("UPSTOX_ACCESS_TOKEN")

api_client = upstox_client.ApiClient(configuration)
api = upstox_client.MarketQuoteApi(api_client)

print("CRUDE SIGNAL BOT V3 STARTED")
print("START TIME:", datetime.now())

# Load old prices if file exists
if os.path.exists(FILE_NAME):
    df_prices = pd.read_csv(FILE_NAME)
    prices = df_prices["price"].tolist()
else:
    prices = []

while True:

    try:

        response = api.ltp(
            "NSE_COM|140106",
            "2.0"
        )

        price = float(
            response.data["NSE_COM:CRUDEOILM26JUNFUT"].last_price
        )

        prices.append(price)

        pd.DataFrame({"price": prices}).to_csv(
            FILE_NAME,
            index=False
        )

        print("--------------------------------")
        print("TIME:", datetime.now())
        print("PRICE:", price)
        print("TOTAL PRICES:", len(prices))

        if len(prices) >= 50:

            df = pd.DataFrame({"close": prices})

            df["EMA20"] = df["close"].ewm(
                span=20,
                adjust=False
            ).mean()

            df["EMA50"] = df["close"].ewm(
                span=50,
                adjust=False
            ).mean()

            ema20 = df["EMA20"].iloc[-1]
            ema50 = df["EMA50"].iloc[-1]

            signal = "BUY" if ema20 > ema50 else "SELL"

            print("EMA20:", round(ema20, 2))
            print("EMA50:", round(ema50, 2))
            print("SIGNAL:", signal)

        else:

            print(
                f"COLLECTING DATA {len(prices)}/50"
            )

        print("--------------------------------")

        time.sleep(30)

    except Exception as e:

        print("ERROR:", str(e))
        time.sleep(30)
