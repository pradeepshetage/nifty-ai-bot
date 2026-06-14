import os
import upstox_client

print("NIFTY QUOTE TEST")

access_token = os.getenv("UPSTOX_ACCESS_TOKEN")

configuration = upstox_client.Configuration()
configuration.access_token = access_token

api_client = upstox_client.ApiClient(configuration)

try:
    print([x for x in dir(upstox_client.MarketQuoteApi) if not x.startswith("_")])
except Exception as e:
    print("ERROR:", e)
