import upstox_client

print(upstox_client.PlaceOrderRequest(
    quantity=75,
    product="D",
    validity="DAY",
    price=0,
    instrument_token="TEST",
    order_type="MARKET",
    transaction_type="BUY"
))
