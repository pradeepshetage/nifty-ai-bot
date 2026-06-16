import os
import upstox_client

ACCESS_TOKEN = os.getenv("UPSTOX_ACCESS_TOKEN")

configuration = upstox_client.Configuration()
configuration.access_token = ACCESS_TOKEN

api_client = upstox_client.ApiClient(configuration)

history_api = upstox_client.HistoryApi(api_client)

try:
    response = history_api.get_historical_candle_data(
        "NSE_INDEX|Nifty 50",
        "day",
        "2025-06-15",
        "2.0"
    )

    print("STATUS")
    print(response.status)

    print(type(response.data))
    print(dir(response.data))

except Exception as e:
    print("FAILED")
    print(str(e))
