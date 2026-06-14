import inspect
import upstox_client

print(inspect.signature(upstox_client.HistoryApi.get_intra_day_candle_data))
