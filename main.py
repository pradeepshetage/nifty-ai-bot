import time

print("UPSTOX SDK TEST")

try:
    import upstox_client
    print("Upstox SDK Installed Successfully")
except Exception as e:
    print("SDK Error:", e)

time.sleep(60)
