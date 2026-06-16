import os
import upstox_client

print("CRUDE BOT STARTED")

ACCESS_TOKEN = os.getenv("UPSTOX_ACCESS_TOKEN")

if ACCESS_TOKEN:
    print("TOKEN FOUND")
else:
    print("TOKEN MISSING")
