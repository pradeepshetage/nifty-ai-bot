import pandas as pd

print("SEARCHING FUTURES")

url = "https://assets.upstox.com/market-quote/instruments/exchange/complete.csv.gz"

df = pd.read_csv(url)

fut = df[
    (df["name"].astype(str).str.contains("CRUDEOILM", case=False, na=False))
]

print("FOUND:", len(fut))

print(
    fut[
        [
            "instrument_key",
            "tradingsymbol",
            "instrument_type",
            "expiry"
        ]
    ].head(20)
)
