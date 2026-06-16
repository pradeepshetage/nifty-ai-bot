import os
import upstox_client

print("UPSTOX SDK CLASSES")
print(dir(upstox_client))

ACCESS_TOKEN = os.getenv("UPSTOX_ACCESS_TOKEN")

configuration = upstox_client.Configuration()
configuration.access_token = ACCESS_TOKEN

api_client = upstox_client.ApiClient(configuration)

history_api = upstox_client.HistoryApi(api_client)


def ema(prices, period):
    multiplier = 2 / (period + 1)

    ema_value = sum(prices[:period]) / period

    for price in prices[period:]:
        ema_value = (price - ema_value) * multiplier + ema_value

    return ema_value


try:
    response = history_api.get_historical_candle_data(
        "NSE_INDEX|Nifty 50",
        "day",
        "2025-06-15",
        "2.0"
    )

    candles = list(reversed(response.data.candles))

    close_prices = [float(candle[4]) for candle in candles]

    print("TOTAL CANDLES:", len(close_prices))
    print("LATEST CLOSE:", close_prices[-1])

    ema20 = ema(close_prices, 20)
    ema50 = ema(close_prices, 50)

    print("EMA20:", round(ema20, 2))
    print("EMA50:", round(ema50, 2))

    if ema20 > ema50:
        print("BUY CE SIGNAL")
    elif ema20 < ema50:
        print("BUY PE SIGNAL")
    else:
        print("NO TRADE")

except Exception as e:
    print("FAILED")
    print(str(e))    close_prices = [float(candle[4]) for candle in candles]

    print("TOTAL CANDLES:", len(close_prices))
    print("LATEST CLOSE:", close_prices[-1])

    ema20 = ema(close_prices, 20)
    ema50 = ema(close_prices, 50)

    print("EMA20:", round(ema20, 2))
    print("EMA50:", round(ema50, 2))

    if ema20 > ema50:
        print("BUY CE SIGNAL")
    elif ema20 < ema50:
        print("BUY PE SIGNAL")
    else:
        print("NO TRADE")

except Exception as e:
    print("FAILED")
    print(str(e))
