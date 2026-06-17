import os
import upstox_client

configuration = upstox_client.Configuration()
configuration.access_token = os.getenv("UPSTOX_ACCESS_TOKEN")

api_client = upstox_client.ApiClient(configuration)

api = upstox_client.InstrumentsApi(api_client)

result = api.search_instrument("CRUDE")

for x in result.data:
    print("================================")
    print("NAME:", x.name)
    print("KEY:", x.instrument_key)
    print("EXPIRY:", x.last_trading_date)
