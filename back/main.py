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
            nurses = [];
            for n in json_data:
                nurses.append(staff.Staff(
                        n['First'], n['Last'], n['Seniority'],
                        n['Charge'], n['Vent'], n['RequestedOn'],
                        n['RequestedOff'], n['RequestedOffSchool'],
                        n['Vacation'], n['Education'], n['Bonus'],n['Title']));

            print("\nMaking schedule.\n")

            s = schedule.Schedule(nurses);
            s.gen_schedule();

            print("Done making schedule. Sending to client.\n")

            await websocket.send(json.dumps(s.json_representation()))

            # print(s)

            # debug.print_week(week, nurses) if DEBUG == True else None;

            print("Checking schedule for invalidations.\n")

            print("Checking schedule for penalties.")

            # for day_idx, day in enumerate(week):
                # penalties = checkschedule.penalties_day(day, day_idx);
                # print("Penalties", penalties);

    start_server = websockets.serve(root, '127.0.0.1', 5678);

    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_server)
    loop.run_forever()
    # nurses = [];
    # with open('../test/nurse.csv', 'r') as csvfile:
        # reader = csv.reader(csvfile, delimiter='|');
        # next(reader) # skip the header
        # # make the array of Nurse objects
        # for l in reader:
            # # Format: 0) First, 1) Last, 2) Seniority, 3) Charge, 4) Vent, 5) RequestedOn,
            # # 6) RequestedOff, 7) RequestedOffSchool, 8) Vacation, 9) Education,
            # # 10) Bonus
            # nurses.append(staff.Nurse(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8],l[9],l[10]));


main()
