import os
import upstox_client

print("HISTORICAL INTERVAL TEST")

ACCESS_TOKEN = os.getenv("UPSTOX_ACCESS_TOKEN")

configuration = upstox_client.Configuration()
configuration.access_token = ACCESS_TOKEN

api_client = upstox_client.ApiClient(configuration)

history_api = upstox_client.HistoryApi(api_client)

try:
    response = history_api.get_historical_candle_data(
        "NSE_COM|140106",
        "30minute",
        "2026-06-17",
        "2.0"
    )

    print("SUCCESS")
    print(len(response.data.candles))

except Exception as e:
    print("ERROR")
    print(str(e))
