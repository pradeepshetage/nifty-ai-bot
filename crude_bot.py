import os
import upstox_client
from pprint import pprint

configuration = upstox_client.Configuration()
configuration.access_token = os.getenv("UPSTOX_ACCESS_TOKEN")

api_client = upstox_client.ApiClient(configuration)
api = upstox_client.MarketQuoteApi(api_client)

contracts = {
    "CRUDE_JUNE": "NSE_COM|140106",
    "CRUDE_JULY": "NSE_COM|149476",
}

for name, instrument in contracts.items():

    print("\n" + "="*50)
    print(name)
    print(instrument)
    print("="*50)

    try:
        response = api.ltp(
            instrument_key=instrument,
            api_version="2.0"
        )

        pprint(response.to_dict())

    except Exception as e:
        print("ERROR:", e)
