import os
import upstox_client

print("UPSTOX PROFILE TEST")

api_key = os.getenv("UPSTOX_API_KEY")
access_token = os.getenv("UPSTOX_ACCESS_TOKEN")

configuration = upstox_client.Configuration()
configuration.access_token = access_token

api_client = upstox_client.ApiClient(configuration)

print("Upstox connection initialized")
