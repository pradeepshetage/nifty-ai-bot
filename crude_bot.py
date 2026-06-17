import os
import time
import pandas as pd
import upstox_client

prices = []

configuration = upstox_client.Configuration()
configuration.access_token = os.getenv("UPSTOX_ACCESS_TOKEN")

api_client = upstox_client.ApiClient(configuration)
api = upstox_client.MarketQuoteApi(api_client)

print("CRUDE SIGNAL BOT STARTED")

while True:

    try:

        response = api.ltp(
            "NSE_COM|140106",
            "2.0"
        )

        price = response.data["NSE_COM:CRUDEOILM26JUNFUT"].last_price

        prices.append(float(price))

        if len(prices) > 100:
            prices.pop(0)

        print("PRICE:", price)

        if len(prices) >= 50:

            df = pd.DataFrame(prices, columns=["close"])

            df["EMA20"] = df["close"].ewm(span=20).mean()
            df["EMA50"] = df["close"].ewm(span=50).mean()

            ema20 = df["EMA20"].iloc[-1]
            ema50 = df["EMA50"].iloc[-1]

            signal = "BUY" if ema20 > ema50 else "SELL"

            print(
                "EMA20:", round(ema20, 2),
                "EMA50:", round(ema50, 2),
                "SIGNAL:", signal
            )

        time.sleep(60)

    except Exception as e:
        print("ERROR:", e)
        time.sleep(60)
