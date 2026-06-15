import upstox_client

for x in dir(upstox_client):
    if "Instrument" in x or "Option" in x:
        print(x)
