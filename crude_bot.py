import os
import upstox_client

configuration = upstox_client.Configuration()
configuration.access_token = os.getenv("UPSTOX_ACCESS_TOKEN")

api_client = upstox_client.ApiClient(configuration)

api = upstox_client.MarketQuoteApi(api_client)

for instrument in [
    "NSE_COM|140106",   # JUN
    "NSE_COM|149476"    # JUL
]:
    try:
        response = api.ltp(
            instrument,
            "2.0"
        )

        print("================================")
        print(instrument)
        print(response)

    except Exception as e:
        print("FAILED:", instrument)
        print(e)
