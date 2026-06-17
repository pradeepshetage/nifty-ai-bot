import os
import upstox_client

configuration = upstox_client.Configuration()
configuration.access_token = os.getenv("UPSTOX_ACCESS_TOKEN")

api_client = upstox_client.ApiClient(configuration)

for name in dir(upstox_client):
    if "Instrument" in name or "instrument" in name:
        print(name)
