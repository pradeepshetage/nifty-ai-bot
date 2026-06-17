import os
import upstox_client
import pandas as pd
from datetime import datetime

print("CRUDE BOT LIVE")

ACCESS_TOKEN = os.getenv("UPSTOX_ACCESS_TOKEN")

configuration = upstox_client.Configuration()
configuration.access_token = ACCESS_TOKEN

api_client = upstox_client.ApiClient(configuration)

history_api = upstox_client.HistoryApi(api_client)

try:
    response = history_api.get_intra_day_candle_data(
        "NSE_COM|140106",
        "5minute",
        "2.0"
    )

    candles = response.data.candles

    df = pd.DataFrame(
        candles,
        columns=["datetime","open","high","low","close","volume","oi"]
    )

    df = df.sort_values("datetime")

    df["EMA20"] = df["close"].ewm(span=20).mean()
    df["EMA50"] = df["close"].ewm(span=50).mean()

    price = df["close"].iloc[-1]
    ema20 = df["EMA20"].iloc[-1]
    ema50 = df["EMA50"].iloc[-1]

    signal = "BUY" if ema20 > ema50 else "SELL"

    print("--------------------------------")
    print("TIME:", datetime.now())
    print("PRICE:", round(price, 2))
    print("EMA20:", round(ema20, 2))
    print("EMA50:", round(ema50, 2))
    print("SIGNAL:", signal)
    print("--------------------------------")

except Exception as e:
    print("ERROR")
    print(str(e))
