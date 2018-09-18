import random, constraints, nurse, debug
""" genweek(ns) accepts arguments:
ns: a list of Nurse objects

genschedule returns a list of lists.
The outermost list corresponds to the days of that week (0-6 -> Sunday -
Saturday).
The inner list corresponds to those nurses (as Nurse objects) who work that day.
"""
def genweek(ns):
    week = [[] for i in range(7)]; # outer list - days; inner list - nurses;
    week = prepopulate(ns, week);
    week = populate(ns, week);
    return week

# Initialize the schedule with days that nurse X has already been decided to
# work day Y
def prepopulate(ns, week):
    day_idx = 0;
    nurse_idx = 0;
    while day_idx < 7:
        # Add nurse to day if already scheduled
        for n in ns:
            if day_idx in n.daysOn:
                week[day_idx].append(n);
        # print(week[day]); # debug
        day_idx += 1; # increment the day

    return week

# populate just tries to find a satisfactory arrangement of nurses to fill out
# the remaining days
def populate(ns, week):
    for day in week:
        av_nurses = list(ns); # list() copies values, not reference
        # remove already-used nurses
        for nurse in ns:
            if nurse in day:
                av_nurses.pop(av_nurses.index(nurse));
        while len(day) < constraints.min_staff_size(day):
            if len(av_nurses) > 0:
                nurse = random.choice(av_nurses);
                day.append(nurse);
                av_nurses.pop(av_nurses.index(nurse)); # remove nurse from consideration
            else:
                break;
        day.sort()
    return week
