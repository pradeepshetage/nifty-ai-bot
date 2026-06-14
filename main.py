import os
import upstox_client

print("UPSTOX ACCOUNT TEST")

access_token = os.getenv("UPSTOX_ACCESS_TOKEN")

configuration = upstox_client.Configuration()
configuration.access_token = access_token

api_client = upstox_client.ApiClient(configuration)

try:
    user_api = upst
