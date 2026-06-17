import upstox_client

for x in dir(upstox_client):
    if "Order" in x:
        print(x)
