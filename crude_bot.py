import os

token = os.getenv("UPSTOX_ACCESS_TOKEN")

print("TOKEN EXISTS:", token is not None)

if token:
    print("TOKEN LENGTH:", len(token))
