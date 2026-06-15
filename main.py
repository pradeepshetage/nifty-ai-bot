import os
import upstox_client

print("CANDLE TEST V3")

ACCESS_TOKEN = os.getenv("UPSTOX_ACCESS_TOKEN")

configuration = upstox_client.Configuration()
configuration.access_token = ACCESS_TOKEN

api_client = upstox_client.ApiClient(configuration)

history_api = upstox_client.HistoryApi(api_client)

try:
    response = history_api.get_intra_day_candle_data(
        "NSE_INDEX|Nifty 50",
        "1minute",
        "2.0"
    )

    print("SUCCESS")
    print(response)

    try:
        print(response.to_dict())
    except Exception as e:
        print("to_dict failed:", str(e))

except Exception as e:
    print("ERROR")
    print(str(e))
