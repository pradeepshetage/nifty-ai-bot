import os
import upstox_client

ACCESS_TOKEN = os.getenv("UPSTOX_ACCESS_TOKEN")

configuration = upstox_client.Configuration()
configuration.access_token = ACCESS_TOKEN

api_client = upstox_client.ApiClient(configuration)

options_api = upstox_client.OptionsApi(api_client)

print("OPTION CONTRACT TEST")

try:
    response = options_api.get_option_contracts(
        "NSE_INDEX|Nifty 50"
    )

    print(response)
    
    try:
        print(response.to_dict())
    except:
        pass

except Exception as e:
    print("ERROR")
    print(str(e))
