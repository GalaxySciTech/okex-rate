import websocket


def on_message(ws, message):
    print(ws)
    print(message)


def on_error(ws, error):
    print(ws)
    print(error)


def on_close(ws):
    print(ws)
    print("### closed ###")


websocket.enableTrace(True)
ws = websocket.WebSocketApp("wss://real.okex.me:8443/ws/v3",
                            on_message=on_message,
                            on_error=on_error,
                            on_close=on_close)

ws.run_forever()