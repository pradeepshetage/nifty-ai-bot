import inspect
import upstox_client

from upstox_client.rest import ApiException

try:
    response = history_api.get_intra_day_candle_data(
        "NSE_INDEX|Nifty 50",
        "5minute",
        "2.0"
    )

    print("SUCCESS")
    print(response)

except ApiException as e:
    print("ERROR")
    print(e)

except Exception as e:
    print("ERROR")
    print(str(e))
