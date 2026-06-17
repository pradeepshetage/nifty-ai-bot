import os
import upstox_client
from pprint import pprint

configuration = upstox_client.Configuration()
configuration.access_token = os.getenv("UPSTOX_ACCESS_TOKEN")

api_client = upstox_client.ApiClient(configuration)

order_api = upstox_client.OrderApi(api_client)

body = upstox_client.PlaceOrderRequest(
    quantity=10,
    product="I",
    validity="DAY",
    price=0,
    instrument_token="MCX_FO|520703",
    order_type="MARKET",
    transaction_type="BUY",
    disclosed_quantity=0,
    trigger_price=0,
    is_amo=False
)

try:
    result = order_api.place_order(
        body,
        "2.0"
    )

    pprint(result)

except Exception as e:
    print("ERROR:")
    print(e)
