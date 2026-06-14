import os
import upstox_client

print("PROFILE FETCH TEST")

access_token = os.getenv("UPSTOX_ACCESS_TOKEN")

configuration = upstox_client.Configuration()
configuration.access_token = access_token

api_client = upstox_client.ApiClient(configuration)

try:
    user_api = upstox_client.UserApi(api_client)

    response = user_api.get_profile()

    print(response)

except Exception as e:
    print("ERROR:", str(e))
