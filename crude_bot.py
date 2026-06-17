import pandas as pd

print("SEARCHING CRUDE")

url = "https://assets.upstox.com/market-quote/instruments/exchange/complete.csv.gz"

df = pd.read_csv(url)

crude = df[
    df["name"].astype(str).str.contains("CRUDE", case=False, na=False)
]

print("FOUND:", len(crude))

print(
    crude[
        [
            "instrument_key",
            "tradingsymbol",
            "name",
            "expiry",
            "instrument_type",
            "exchange"
        ]
    ].head(50).to_string()
