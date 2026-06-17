import os
import upstox_client

print("LTP TEST")

configuration = upstox_client.Configuration()
configuration.access_token = os.getenv("UPSTOX_ACCESS_TOKEN")

api_client = upstox_client.ApiClient(configuration)

api = upstox_client.MarketQuoteApi(api_client)

try:
    response = api.ltp(
        "NSE_COM|140106",
        "2.0"
    )

    print("SUCCESS")
    print(response)

except Exception as e:
    print("ERROR")
    print(type(e))
    print(str(e))
