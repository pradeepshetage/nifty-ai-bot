import os
import upstox_client
from pprint import pprint
from upstox_client.rest import ApiException

# Better configuration
configuration = upstox_client.Configuration()
configuration.access_token = os.getenv("UPSTOX_ACCESS_TOKEN")

# Optional: Set host if needed (usually not required)
# configuration.host = "https://api.upstox.com"

api_client = upstox_client.ApiClient(configuration)
order_api = upstox_client.OrderApi(api_client)

body = upstox_client.PlaceOrderRequest(   # or PlaceOrderV3Request if using v3
    quantity=10,
    product="I",                    # I = Intraday
    validity="DAY",
    price=0,
    instrument_token="MCX_FO|520703",
    order_type="MARKET",
    transaction_type="BUY",
    disclosed_quantity=0,
    trigger_price=0,
    is_amo=False,
    # tag="your-bot-tag",           # Recommended: helps tracking
)

try:
    result = order_api.place_order(body, "2.0")   # or "3.0" for newer version
    pprint(result)
except ApiException as e:          # Better exception handling
    print("API Exception:")
    print(f"Status: {e.status}")
    print(f"Reason: {e.reason}")
    print(f"Body: {e.body}")
except Exception as e:
    print("General ERROR:")
    print(e)
