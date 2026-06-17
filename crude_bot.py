import os
import upstox_client
from pprint import pprint

configuration = upstox_client.Configuration()
configuration.access_token = os.getenv("UPSTOX_ACCESS_TOKEN")

api_client = upstox_client.ApiClient(configuration)
api = upstox_client.MarketQuoteApi(api_client)

response = api.get_full_market_quote(
    "NSE_COM|140106",
    "2.0"
)

pprint(response.to_dict())
