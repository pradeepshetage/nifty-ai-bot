import os
import upstox_client

print("UPSTOX USER PROFILE TEST")

access_token = os.getenv("UPSTOX_ACCESS_TOKEN")

configuration = upstox_client.Configuration()
configuration.access_token = access_token

api_client = upstox_client.ApiClient(configuration)

try:
    print("SDK Connected Successfully")
except Exception as e:
    print("Error:", e)
