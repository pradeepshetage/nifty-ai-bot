import os
import upstox_client

ACCESS_TOKEN = os.getenv("UPSTOX_ACCESS_TOKEN")

configuration = upstox_client.Configuration()
configuration.access_token = ACCESS_TOKEN

api_client = upstox_client.ApiClient(configuration)

history_api = upstox_client.HistoryApi(api_client)

try:
    response = history_api.get_historical_candle_data(
        "NSE_INDEX|Nifty 50",
        "day",
        "2025-06-15",
        "2.0"
    )

    candles = response.data.candles

    print("TOTAL CANDLES:", len(candles))

    if len(candles) > 0:
        print("FIRST CANDLE:")
        print(candles[0])

        print("LAST CANDLE:")
        print(candles[-1])

except Exception as e:
    print("FAILED")
    print(str(e))
