import os
import upstox_client

print("INTRADAY DEBUG")

ACCESS_TOKEN = os.getenv("UPSTOX_ACCESS_TOKEN")

configuration = upstox_client.Configuration()
configuration.access_token = ACCESS_TOKEN

api_client = upstox_client.ApiClient(configuration)

history_api = upstox_client.HistoryApi(api_client)

try:
    response = history_api.get_intra_day_candle_data(
        "NSE_COM|140106",
        "1minute",
        "2.0"
    )

    print("SUCCESS")
    print(response)

except Exception as e:
    print("ERROR")
    print(type(e))
    print(str(e))
