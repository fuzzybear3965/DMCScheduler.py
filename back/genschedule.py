import random, constraints, schedule

def genschedule(ns):
    s = initschedule(ns);
    return s

def initschedule(ns):
    s = schedule.Schedule();
    s.weeks = [schedule.Week(ns) for i in range(4)]
    
    # Add nurses to their requested days
    for n in ns:
        for d in n.daysRequestedOn:
            week_idx = d // 7;
            day_idx = d % 7;
            s.weeks[week_idx].days[day_idx].nurses.append(n)
    return s
