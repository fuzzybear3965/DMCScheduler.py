#!/usr/bin/env python

#!/usr/bin/env python

# WS server that sends messages at random intervals

import asyncio
import websockets
import signal
import json

signal.signal(signal.SIGINT, signal.SIG_DFL)

async def root(websocket, path):
    print("New Client.")
    while True:
        try:
            string_data = await websocket.recv()
            json_data = json.loads(string_data);
        except websockets.exceptions.ConnectionClosed:
            print("Client closed connection.")
            break;
        print("Received {0}.".format(json_data["meta"]["fields"]))

start_server = websockets.serve(root, '127.0.0.1', 5678)

loop = asyncio.get_event_loop()
loop.run_until_complete(start_server)
loop.run_forever()

# try: 
# except KeyboardInterrupt:
    # raise
# except:
    # print("Received exit, exiting.")
