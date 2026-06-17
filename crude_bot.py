import os
import upstox_client

print("OHLC TEST")

configuration = upstox_client.Configuration()
configuration.access_token = os.getenv("UPSTOX_ACCESS_TOKEN")

api_client = upstox_client.ApiClient(configuration)

api = upstox_client.MarketQuoteApi(api_client)

try:
    response = api.get_market_quote_ohlc(
        "NSE_COM|140106",
        "I1",
        "2.0"
    )

    print("SUCCESS")
    print(response)

except Exception as e:
    print("ERROR")
    print(type(e))
    print(str(e))
