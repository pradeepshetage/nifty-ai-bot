import os
import pandas as pd
import upstox_client

print("NIFTY AI BOT")

ACCESS_TOKEN = os.getenv("UPSTOX_ACCESS_TOKEN")

configuration = upstox_client.Configuration()
configuration.access_token = ACCESS_TOKEN

api_client = upstox_client.ApiClient(configuration)

history_api = upstox_client.HistoryApi(api_client)

response = history_api.get_intra_day_candle_data(
    "NSE_INDEX|Nifty 50",
    "1minute",
    "2.0"
)

candles = response.to_dict()["data"]["candles"]

df = pd.DataFrame(
    candles,
    columns=[
        "timestamp",
        "open",
        "high",
        "low",
        "close",
        "volume",
        "oi"
    ]
)

df = df.iloc[::-1]

df["EMA20"] = df["close"].ewm(span=20).mean()
df["EMA50"] = df["close"].ewm(span=50).mean()

latest = df.iloc[-1]

print("PRICE :", latest["close"])
print("EMA20 :", round(latest["EMA20"],2))
print("EMA50 :", round(latest["EMA50"],2))

if latest["EMA20"] > latest["EMA50"]:
    print("SIGNAL : BUY CE")

elif latest["EMA20"] < latest["EMA50"]:
    print("SIGNAL : BUY PE")

else:
    print("SIGNAL : NO TRADE")
