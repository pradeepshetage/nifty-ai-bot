import os
import upstox_client
from pprint import pprint

configuration = upstox_client.Configuration()
configuration.access_token = os.getenv("UPSTOX_ACCESS_TOKEN")

api_client = upstox_client.ApiClient(configuration)

api = upstox_client.InstrumentsApi(api_client)

try:
    result = api.search_instrument(
        "MCX",
        "CRUDEOILM"
    )

    pprint(result)

except Exception as e:
    print("ERROR")
    print(type(e))
    print(e)
