import os

print("UPSTOX CONNECTION TEST")

api_key = os.getenv("UPSTOX_API_KEY")
access_token = os.getenv("UPSTOX_ACCESS_TOKEN")

print("API Key Loaded:", bool(api_key))
print("Access Token Loaded:", bool(access_token))
