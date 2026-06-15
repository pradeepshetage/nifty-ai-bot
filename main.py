import inspect
import upstox_client

print("OPTION CHAIN SIGNATURE")
print(inspect.signature(upstox_client.OptionsApi.get_put_call_option_chain))

print("OPTION CONTRACT SIGNATURE")
print(inspect.signature(upstox_client.OptionsApi.get_option_contracts))
