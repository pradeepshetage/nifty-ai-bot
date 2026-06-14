import os
import upstox_client

print("UPSTOX PROFILE API TEST")

access_token = os.getenv("UPSTOX_ACCESS_TOKEN")

configuration = upstox_client.Configuration()
configuration.access_token = access_token

api_client = upstox_client.ApiClient(configuration)

print("SDK Connected Successfully")

print([x for x in dir(upstox_client) if "User" in x])
