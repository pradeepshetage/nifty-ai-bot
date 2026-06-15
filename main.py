import os
import upstox_client

ACCESS_TOKEN = os.getenv("UPSTOX_ACCESS_TOKEN")

configuration = upstox_client.Configuration()
configuration.access_token = ACCESS_TOKEN

api_client = upstox_client.ApiClient(configuration)

user_api = upstox_client.UserApi(api_client)

print("PROFILE TEST")

try:
    response = user_api.get_profile("2.0")
    print(response)
except Exception as e:
    print(e)
