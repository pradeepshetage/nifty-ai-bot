import upstox_client

print([x for x in dir(upstox_client) if "History" in x or "Candle" in x])
