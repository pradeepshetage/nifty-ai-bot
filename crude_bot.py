import os
import upstox_client
import pandas as pd

print("CRUDE DATA CHECK")

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
    columns=["datetime", "open", "high", "low", "close", "volume", "oi"]
)

print("TOTAL CANDLES:", len(df))

print("\nFIRST 5 CANDLES")
print(df[["datetime", "open", "high", "low", "close"]].head())

print("\nLAST 5 CANDLES")
print(df[["datetime", "open", "high", "low", "close"]].tail())
