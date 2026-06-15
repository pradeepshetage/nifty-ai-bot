import upstox_client

print("INSTRUMENT SEARCH")

for x in dir(upstox_client):
    if "Instrument" in x:
        print(x)

for x in dir(upstox_client):
    if "Option" in x:
        print(x)
