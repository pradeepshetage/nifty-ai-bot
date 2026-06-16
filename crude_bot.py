import os
import upstox_client

print("CRUDE BOT STARTED")

ACCESS_TOKEN = os.getenv("UPSTOX_ACCESS_TOKEN")

configuration = upstox_client.Configuration()
configuration.access_token = ACCESS_TOKEN

api_client = upstox_client.ApiClient(configuration)

history_api = upstox_client.HistoryApi(api_client)

try:
    response = history_api.get_historical_candle_data(
        "MCX_FO|CRUDEOILM",
        "day",
        "2025-06-15",
        "2.0"
    )

    print("SUCCESS")
    print("TOTAL CANDLES:", len(response.data.candles))

except Exception as e:
    print("FAILED")
    print(type(e))
    print(repr(e))
