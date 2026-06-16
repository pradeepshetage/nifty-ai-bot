import os
import upstox_client

print("CRUDE BOT STARTED")

ACCESS_TOKEN = os.getenv("UPSTOX_ACCESS_TOKEN")

configuration = upstox_client.Configuration()
configuration.access_token = ACCESS_TOKEN

api_client = upstox_client.ApiClient(configuration)

history_api = upstox_client.HistoryApi(api_client)

print("UPSTOX CONNECTED")

print(dir(history_api))
