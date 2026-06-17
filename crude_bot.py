import os

token = os.getenv("UPSTOX_ACCESS_TOKEN")

print("START")
print("FIRST 20:", token[:20])
print("LAST 20:", token[-20:])
print("LENGTH:", len(token))
print("END")
