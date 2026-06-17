import os
import upstox_client

print("CRUDE TEST")

ACCESS_TOKEN = os.getenv("UPSTOX_ACCESS_TOKEN")

configuration = upstox_client.Configuration()
configuration.access_token = ACCESS_TOKEN

api_client = upstox_client.ApiClient(configuration)

history_api = upstox_client.HistoryApi(api_client)

keys = [
    "MCX_FO|CRUDEOILM",
    "MCX_COM|CRUDEOILM",
    "MCX_FO|CRUDEOIL",
    "MCX_COM|CRUDEOIL"
]

for key in keys:
    try:
        response = history_api.get_historical_candle_data(
            key,
            "day",
            "2025-06-15",
            "2.0"
        )

        print("SUCCESS:", key)
        print(len(response.data.candles))

    except Exception as e:
        print("FAILED:", key)
