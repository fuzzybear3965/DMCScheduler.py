from ._calendar import Week
from functools import reduce
import random

def gen_schedule(self):
    _init_schedule(self);
    _cull_schedule(self);
    _populate_schedule(self);
    _record_staff_days(self);

# init_schedule adds nurses to those days they have requested
def _init_schedule(schedule):
    schedule.weeks = [Week(schedule.nurses) for i in range(4)]
    # Add nurses to their requested days
    for n in schedule.nurses:
        for d in n.daysRequestedOn:
            week_idx = d // 7;
            day_idx = d % 7;
            schedule.weeks[week_idx].days[day_idx].nurses.append(n)

# cull_schedule removes nurses of low seniority from weekdays and high seniority
# from weekends. It reduces the maximum number of nurses to the minimum required
# for all days. populate_schedule adds more nurses to certain days
def _cull_schedule(schedule):
    day = 0;
    for w in schedule.weeks:
        for d in w.days:
            # TODO: Make number of staff per day something user-configurable
            if len(d.nurses) > 7:
                # arrange nurses by seniority
                seniorities = [x.seniority for x in d.nurses]
                # taken from https://stackoverflow.com/questions/6618515/sorting-list-based-on-values-from-another-list
                d.nurses = [x for _,x in sorted(zip(seniorities, d.nurses), key=lambda pair: pair[0])]
                # too many weekend people, keep the low seniority folk
                if day % 7 in (1,5):
                    d.nurses = d.nurses[0:7]
                else:
                    d.nurses = d.nurses[-7:]
            day += 1;

# pop_schedule adds random eligible nurses of high seniority to understaffed
# weekdays and random eligible nurses of low seniority to understaffed weekends.
# Mondays and Fridays receive a random number of extra nurses to compensate for
# frequent sick days
def _populate_schedule(schedule):
    day = 0;
    for w in schedule.weeks:
        for d in w.days:
            if len(d) < 7:
                eligible_nurses = [];
                for n in schedule.nurses:
                    if day not in n.daysRequestedOff + n.daysRequestedOffSchool + n.daysVacation:
                        eligible_nurses.append(n);
                if day % 7 in (1,5): # monday/friday need 8+ people
                    print("Day {0} is understaffed with {1} staff members.".format(day, len(d)))
                    num_needed = 8-len(d);
                    selected_nurses = _weighted_select_n(
                            eligible_nurses, num_needed
                            );
                    d.nurses.extend(selected_nurses);
                    print('selected {0} additional staff for day {1}.'.format(len(selected_nurses), day))
                else: # weekdays need 7+
                    print("Day {0} is understaffed with {1} staff members.".format(day, len(d)))
                    num_needed = 7-len(d);
                    selected_nurses = _weighted_select_n(
                            eligible_nurses, num_needed
                            );
                    d.nurses.extend(selected_nurses);
            day += 1;
# record_staff_days records the schedhuled days of each staff member in the
# object corresponding to each staff member.
def _record_staff_days(s):
    day = 0;
    for w in s.weeks:
        for d in w.days:
            for staff in d.nurses:
                staff.daysScheduled.append(day);
            day += 1;


def _weighted_select_n(lst, n):
    weights = _weights_from_seniorities(lst);
    res = [];
    for i in range(n):
        chosen = _weighted_choice(lst, weights);
        res.append(chosen);
        # remove chosen from list and update weights
        lst.pop(lst.index(chosen));
        weights = _weights_from_seniorities(lst);
    return res

# taken from https://scaron.info/blog/python-weighted-choice.html
def _weighted_choice(seq, weights):
    assert len(weights) == len(seq)
    assert abs(1. - sum(weights)) < 1e-6

    x = random.random()
    for i, elmt in enumerate(seq):
        if x <= weights[i]:
            return elmt
        x -= weights[i]

def _weights_from_seniorities(lst):
    total_weight = reduce(lambda x,y : x + y, [1./el.seniority for el in lst])
    return list(map(lambda x: x/total_weight, [1./el.seniority for el in lst]))
