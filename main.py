import os
import upstox_client

print("TOKEN TEST")

ACCESS_TOKEN = os.getenv("UPSTOX_ACCESS_TOKEN")

configuration = upstox_client.Configuration()
configuration.access_token = ACCESS_TOKEN

api_client = upstox_client.ApiClient(configuration)

history_api = upstox_client.HistoryApi(api_client)

try:
    print(dir(history_api))
    
    response = history_api.get_intra_day_candle_data(
        "NSE_INDEX|Nifty 50",
        "1minute",
        "2.0"
    )

    print("CANDLE SUCCESS")
    print("CANDLE DATA")
    print(response)

except Exception as e:
    print("CANDLE FAILED")
    print(str(e))
