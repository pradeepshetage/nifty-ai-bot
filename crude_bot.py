import os
import upstox_client
import pandas as pd

print("CRUDE EMA TEST")

ACCESS_TOKEN = os.getenv("UPSTOX_ACCESS_TOKEN")

configuration = upstox_client.Configuration()
configuration.access_token = ACCESS_TOKEN

api_client = upstox_client.ApiClient(configuration)

history_api = upstox_client.HistoryApi(api_client)

response = history_api.get_historical_candle_data(
    "NSE_COM|149476",
    "day",
    "2026-06-17",
    "2.0"
)

candles = response.data.candles

df = pd.DataFrame(
    candles,
    columns=["datetime","open","high","low","close","volume","oi"]
)

df["EMA20"] = df["close"].ewm(span=20).mean()
df["EMA50"] = df["close"].ewm(span=50).mean()

print("TOTAL CANDLES:", len(df))
print("LAST CLOSE:", df["close"].iloc[-1])
print("EMA20:", round(df["EMA20"].iloc[-1],2))
print("EMA50:", round(df["EMA50"].iloc[-1],2))
