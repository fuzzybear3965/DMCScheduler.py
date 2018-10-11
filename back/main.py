import csv, staff, genschedule, checkschedule, constraints, debug

DEBUG = True;

def main():
    nurses = [];
    with open('../test/nurse.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter='|');
        next(reader) # skip the header
        # make the array of Nurse objects
        for l in reader:
            # Format: 0) First, 1) Last, 2) Seniority, 3) Charge, 4) Vent, 5) RequestedOn,
            # 6) RequestedOff, 7) RequestedOffSchool, 8) Vacation, 9) Education,
            # 10) Bonus
            nurses.append(staff.Nurse(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8],l[9],l[10]));

        print("\nMaking schedule.\n")

        schedule = genschedule.genschedule(nurses);

        print("Done making schedule. Printing.\n")

        print(schedule)

        # debug.print_week(week, nurses) if DEBUG == True else None;

        print("Checking schedule for invalidations.\n")

        print("Checking schedule for penalties.")

        # for day_idx, day in enumerate(week):
            # penalties = checkschedule.penalties_day(day, day_idx);
            # print("Penalties", penalties);

main()
