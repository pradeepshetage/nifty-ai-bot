import os
import upstox_client

print("USER API METHODS TEST")

access_token = os.getenv("UPSTOX_ACCESS_TOKEN")

configuration = upstox_client.Configuration()
configuration.access_token = access_token

api_client = upstox_client.ApiClient(configuration)

user_api = upstox_client.UserApi(api_client)

print(dir(user_api))
