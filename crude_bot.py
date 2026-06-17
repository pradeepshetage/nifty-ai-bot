import pandas as pd

print("DOWNLOADING MASTER FILE")

url = "https://assets.upstox.com/market-quote/instruments/exchange/complete.csv.gz"

df = pd.read_csv(url)

print("ROWS:", len(df))
print("COLUMNS:")
print(df.columns.tolist())
