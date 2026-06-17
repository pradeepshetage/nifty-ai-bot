import os
import upstox_client
import pandas as pd
from datetime import datetime

print("CRUDE JULY TEST")

ACCESS_TOKEN = os.getenv("UPSTOX_ACCESS_TOKEN")

configuration = upstox_client.Configuration()
configuration.access_token = ACCESS_TOKEN

api_client = upstox_client.ApiClient(configuration)

history_api = upstox_client.HistoryApi(api_client)

try:

    response = history_api.get_historical_candle_data(
        "NSE_COM|149476",   # CRUDEOILM26JULFUT
        "30minute",
        "2026-06-17",
        "2.0"
    )

    candles = response.data.candles

    print("TOTAL CANDLES:", len(candles))

    if len(candles) == 0:
        print("NO DATA RETURNED")
    else:

        df = pd.DataFrame(
            candles,
            columns=[
                "datetime",
                "open",
                "high",
                "low",
                "close",
                "volume",
                "oi"
            ]
        )

        df = df.sort_values("datetime")

        print("\nFIRST CANDLE")
        print(df.iloc[0])

        print("\nLAST CANDLE")
        print(df.iloc[-1])

        print("\nLATEST DATETIME")
        print(df.iloc[-1]["datetime"])

        print("\nLATEST CLOSE")
        print(df.iloc[-1]["close"])

        df["EMA20"] = df["close"].ewm(span=20).mean()
        df["EMA50"] = df["close"].ewm(span=50).mean()

        price = float(df["close"].iloc[-1])
        ema20 = float(df["EMA20"].iloc[-1])
        ema50 = float(df["EMA50"].iloc[-1])

        signal = "BUY" if ema20 > ema50 else "SELL"

        print("\n----------------------------")
        print("TIME:", datetime.now())
        print("PRICE:", round(price, 2))
        print("EMA20:", round(ema20, 2))
        print("EMA50:", round(ema50, 2))
        print("SIGNAL:", signal)
        print("----------------------------")

except Exception as e:
    print("ERROR")
    print(type(e))
    print(str(e))
