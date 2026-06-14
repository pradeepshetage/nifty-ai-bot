import os
import upstox_client

print("NIFTY CANDLE TEST")

access_token = os.getenv("UPSTOX_ACCESS_TOKEN")

configuration = upstox_client.Configuration()
configuration.access_token = access_token

api_client = upstox_client.ApiClient(configuration)

try:
    history_api = upstox_client.HistoryApi(api_client)

    print(dir(history_api))

except Exception as e:
    print("ERROR:", str(e))
