import os
import upstox_client

configuration = upstox_client.Configuration()
configuration.access_token = os.getenv("UPSTOX_ACCESS_TOKEN")

api_client = upstox_client.ApiClient(configuration)

api = upstox_client.MarketQuoteApi(api_client)

print(api.ltp.__doc__)
