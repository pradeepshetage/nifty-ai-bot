import os
import upstox_client

print("TOKEN TEST")

ACCESS_TOKEN = os.getenv("UPSTOX_ACCESS_TOKEN")

configuration = upstox_client.Configuration()
configuration.access_token = ACCESS_TOKEN

api_client = upstox_client.ApiClient(configuration)

api = upstox_client.UserApi(api_client)

try:
    response = api.get_profile("2.0")

    print("SUCCESS")
    print(response)

except Exception as e:
    print("FAILED")
    print(type(e))
    print(str(e))
