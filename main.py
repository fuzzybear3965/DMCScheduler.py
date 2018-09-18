import csv, nurse, genschedule, checkschedule, constraints, debug

DEBUG = True;

def main():
    nurses = [];
    with open('nurse.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter='|');
        next(reader) # skip the header
        # make the array of Nurse objects
        for l in reader:
            nurses.append(nurse.Nurse(l[0],l[1],l[2],l[3],l[4],l[5]));

        print("\nMaking schedule.\n")

        week = genschedule.genweek(nurses)

        print("Done making schedule. Printing.\n")

        debug.print_week(week, nurses) if DEBUG == True else None;

        print("Checking schedule for invalidations.")

        print("Checking schedule for penalties.")

        for day_idx, day in enumerate(week):
            penalties = checkschedule.penalties_day(day, day_idx);
            print("Penalties", penalties)

main()
