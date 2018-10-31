#!/usr/bin/env python

# WS server that sends messages at random intervals

import asyncio
import websockets
import signal
import json
import csv, staff, schedule, constraints, debug

signal.signal(signal.SIGINT, signal.SIG_DFL)


DEBUG = True;
def main():

    async def root(websocket, path):
        print("New Client.")
        while True:
            try:
                string_data = await websocket.recv()
            except websockets.exceptions.ConnectionClosed:
                print("Client closed connection.")
                break;
            json_data = json.loads(string_data);
            personnel = [];
            for n in json_data:
                personnel.append(staff.Staff(
                        n['First'], n['Last'], n['Seniority'],
                        n['WeekendType'],
                        n['Charge'], n['Vent'], n['RequestedOn'],
                        n['RequestedOff'], n['RequestedOffSchool'],
                        n['Vacation'], n['Education'], n['Bonus']));

            print("\nMaking schedule.\n");

            s = schedule.Schedule(personnel);
            s.gen_schedule();

            print("Done making schedule. Sending to client.\n")

            await websocket.send(json.dumps(s.json_representation()))

            # print(s)

            # debug.print_week(week, personnel) if DEBUG == True else None;

            print("Checking schedule for invalidations.\n")

            print("Checking schedule for penalties.")

            # for day_idx, day in enumerate(week):
                # penalties = checkschedule.penalties_day(day, day_idx);
                # print("Penalties", penalties);

    start_server = websockets.serve(root, '127.0.0.1', 5678);

    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_server)
    loop.run_forever()

main()
