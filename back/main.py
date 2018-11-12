#!/usr/bin/env python

# WS server that sends messages at random intervals

import asyncio
import websockets
import signal
import json
from . import staff, schedule

signal.signal(signal.SIGINT, signal.SIG_DFL)

DEBUG = True


def main():

    async def root(ws, _):
        print("New Client.")
        while True:
            try:
                string_data = await ws.recv()
            except ws.exceptions.ConnectionClosed:
                print("Client closed connection.")
                break
            json_data = json.loads(string_data)
            personnel = []
            for n in json_data:
                days = []
                for i in range(28):
                    days.append(n[str(i)])
                personnel.append(staff.Staff(
                        n['First'], n['Last'], n['Seniority'],
                        n['WeekendType'],
                        n['Charge'], n['Vent'], days))

            print("\nMaking schedule.\n")

            s = schedule.Schedule(personnel)
            s.gen_schedule()

            print("Checking schedule for penalties.\n")

            s.check_schedule()

            print("Sending to client.\n")
            await ws.send(json.dumps(s.json_representation()))

    start_server = websockets.serve(root, '127.0.0.1', 5678)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_server)
    loop.run_forever()


main()
