import os
import upstox_client

print("MARKET API METHODS")

ACCESS_TOKEN = os.getenv("UPSTOX_ACCESS_TOKEN")

configuration = upstox_client.Configuration()
configuration.access_token = ACCESS_TOKEN

api_client = upstox_client.ApiClient(configuration)

api = upstox_client.MarketQuoteApi(api_client)

print(dir(api))
