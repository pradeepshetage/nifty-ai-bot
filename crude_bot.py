import os
import upstox_client

ACCESS_TOKEN = os.getenv("UPSTOX_ACCESS_TOKEN")

configuration = upstox_client.Configuration()
configuration.access_token = ACCESS_TOKEN

api_client = upstox_client.ApiClient(configuration)

instruments_api = upstox_client.InstrumentsApi(api_client)

response = instruments_api.search_instrument("CRUDEOIL")

print(response)
