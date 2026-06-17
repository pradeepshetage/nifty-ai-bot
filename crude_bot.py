import pandas as pd

print("ACTIVE CRUDE CONTRACTS")

url = "https://assets.upstox.com/market-quote/instruments/exchange/complete.csv.gz"

df = pd.read_csv(url)

crude = df[
    (df["name"].astype(str).str.contains("CRUDEOILM", case=False, na=False))
]

print(
    crude[
        [
            "instrument_key",
            "tradingsymbol",
            "expiry",
            "instrument_type"
        ]
    ].to_string()
)
