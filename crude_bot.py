import os
import upstox_client

print("CRUDE BOT STARTED")

ACCESS_TOKEN = os.getenv("UPSTOX_ACCESS_TOKEN")

configuration = upstox_client.Configuration()
configuration.access_token = ACCESS_TOKEN

api_client = upstox_client.ApiClient(configuration)

instruments_api = upstox_client.InstrumentsApi(api_client)

print(dir(instruments_api))
print(instruments_api.search_instrument.__doc__)
