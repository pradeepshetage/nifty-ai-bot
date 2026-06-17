import os
import upstox_client

ACCESS_TOKEN = os.getenv("UPSTOX_ACCESS_TOKEN")

configuration = upstox_client.Configuration()
configuration.access_token = ACCESS_TOKEN

api_client = upstox_client.ApiClient(configuration)

api = upstox_client.UserApi(api_client)

print(api.get_profile("2.0"))
