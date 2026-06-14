import os

print("DURVANG TEST 123")

api_key = os.getenv("UPSTOX_API_KEY")
access_token = os.getenv("UPSTOX_ACCESS_TOKEN")

if api_key:
    print("API Key Loaded Successfully")
else:
    print("API Key Missing")

if access_token:
    print("Access Token Loaded Successfully")
else:
    print("Access Token Missing")
