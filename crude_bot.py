import os
import upstox_client
from pprint import pprint

configuration = upstox_client.Configuration()
configuration.access_token = os.getenv("UPSTOX_ACCESS_TOKEN")

api_client = upstox_client.ApiClient(configuration)
api = upstox_client.MarketQuoteApi(api_client)

contracts = [
    "NSE_COM|140106",  # June
    "NSE_COM|149476"   # July
]

for symbol in contracts:

    print("\n" + "="*50)
    print("TESTING:", symbol)

    try:

        response = api.ltp(
            symbol,
            "2.0"
        )

        pprint(response.to_dict())

    except Exception as e:

        print("ERROR:", e)
