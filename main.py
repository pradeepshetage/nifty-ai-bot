import os
import upstox_client

print("LIVE NIFTY TEST")

access_token = os.getenv("UPSTOX_ACCESS_TOKEN")

configuration = upstox_client.Configuration()
configuration.access_token = access_token

api_client = upstox_client.ApiClient(configuration)

try:
    quote_api = upstox_client.MarketQuoteApi(api_client)

    response = quote_api.ltp(
        "NSE_INDEX|Nifty 50",
        "2.0"
    )

    print(response)

except Exception as e:
    print("ERROR:", str(e))
