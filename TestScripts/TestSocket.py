import websocket
try:
    import thread
except ImportError:
    import _thread as thread
import time

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        for i in range(100):
            time.sleep(1)
            ws.send('42["selection",{"ranges":[{"anchor":0,"head":0}]}]')
            ws.send('42["operation",83,["hello",188],{"ranges":[{"anchor":1,"head":1}]}]')
        time.sleep(1)
        #ws.close()
        print("thread terminating...")
    ws.send('42["login",{"name":"xxx"}]')
    thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://127.0.0.1:3000/socket.io/?EIO=3&transport=websocket",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
