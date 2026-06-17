import os
import upstox_client
import time

configuration = upstox_client.Configuration()
configuration.access_token = os.getenv("UPSTOX_ACCESS_TOKEN")

api_client = upstox_client.ApiClient(configuration)
api = upstox_client.MarketQuoteApi(api_client)

for i in range(5):

    response = api.ltp(
        "NSE_COM|140106",
        "2.0"
    )

    print(response)

    time.sleep(10)
