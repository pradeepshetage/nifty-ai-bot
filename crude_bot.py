import os
import upstox_client

print("CRUDE FUT TEST")

ACCESS_TOKEN = os.getenv("UPSTOX_ACCESS_TOKEN")

configuration = upstox_client.Configuration()
configuration.access_token = ACCESS_TOKEN

api_client = upstox_client.ApiClient(configuration)

history_api = upstox_client.HistoryApi(api_client)

response = history_api.get_historical_candle_data(
    "NSE_COM|149476",
    "day",
    "2025-06-15",
    "2.0"
)

print("SUCCESS")
print("CANDLES:", len(response.data.candles))
