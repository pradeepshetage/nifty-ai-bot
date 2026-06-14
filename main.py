import upstox_client

print([x for x in dir(upstox_client) if "Market" in x or "Quote" in x or "History" in x])
