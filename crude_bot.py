import os
import time
import pandas as pd
import upstox_client
from datetime import datetime

prices = []

configuration = upstox_client.Configuration()
configuration.access_token = os.getenv("UPSTOX_ACCESS_TOKEN")

api_client = upstox_client.ApiClient(configuration)
api = upstox_client.MarketQuoteApi(api_client)

print("CRUDE SIGNAL BOT V2 STARTED")

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

        if len(prices) > 100:
            prices.pop(0)

        print(
            f"{datetime.now()} | PRICE: {price}"
        )

        if len(prices) >= 50:

            df = pd.DataFrame(prices, columns=["close"])

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

            print(
                f"EMA20={ema20:.2f} "
                f"EMA50={ema50:.2f} "
                f"SIGNAL={signal}"
            )

        else:
            print(
                f"Collecting data... "
                f"{len(prices)}/50"
            )

        time.sleep(30)

    except Exception as e:

        print("ERROR:", str(e))
        time.sleep(30)
