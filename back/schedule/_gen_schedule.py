from ._calendar import Week
from functools import reduce
import random

def gen_schedule(self):
    _init_schedule(self);
    _cull_schedule(self);
    _populate_schedule(self);
    _record_staff_days(self);

# init_schedule adds staff to those days they have requested
def _init_schedule(schedule):
    schedule.weeks = [Week(schedule.staff) for i in range(4)]
    # Add staff to their requested days
    for n in schedule.staff:
        for d in n.daysRequestedOn:
            week_idx = d // 7;
            day_idx = d % 7;
            schedule.weeks[week_idx].days[day_idx].staff.append(n)

# cull_schedule removes staff of low seniority from weekdays and high seniority
# from weekends. It reduces the maximum number of staff to the minimum required
# for all days. populate_schedule adds more staff to certain days
def _cull_schedule(schedule):
    day = 0;
    for w in schedule.weeks:
        for d in w.days:
            # TODO: Make number of staff per day something user-configurable
            if len(d.staff) > 7:
                # arrange staff by seniority
                seniorities = [x.seniority for x in d.staff]
                # taken from https://stackoverflow.com/questions/6618515/sorting-list-based-on-values-from-another-list
                d.staff = [x for _,x in sorted(zip(seniorities, d.staff), key=lambda pair: pair[0])]
                # too many weekend people, keep the low seniority folk
                if day % 7 in (1,5):
                    d.staff = d.staff[0:7]
                else:
                    d.staff = d.staff[-7:]
            day += 1;

# pop_schedule adds random eligible staff of high seniority to understaffed
# weekdays and random eligible staff of low seniority to understaffed weekends.
# Mondays and Fridays receive a random number of extra staff to compensate for
# frequent sick days
def _populate_schedule(s):
    day = 0;
    for w in s.weeks:
        for d in w.days:
            weekend_understaffed = (day % 7 in (0,5,6)) and (len(d) < 8);
            weekday_understaffed = (day % 7 not in (0,5,6)) and (len(d) < 7);
            is_understaffed = weekday_understaffed or weekend_understaffed;
            if is_understaffed:
                eligible_staff = [];
                if weekend_understaffed: # monday/friday need 8+ people
                    if (day%14 in (0,12,13)): # A-type weekend
                        for staff in s.staff:
                            if staff not in d and not _has_day_off(staff, day):
                                if staff.weekendType == 'A':
                                    eligible_staff.append(staff);
                    else: # B-type weekend
                        for staff in s.staff:
                            if staff not in d and not _has_day_off(staff, day):
                                if staff.weekendType == 'B':
                                    eligible_staff.append(staff);

                    num_needed = 8-len(d);

                    selected_staff = _weighted_select_n(
                            eligible_staff, num_needed, invert=True
                            );
                    d.staff.extend(selected_staff);
                else: # weekdays need 7+
                    num_needed = 7-len(d);
                    selected_staff = _weighted_select_n(
                            eligible_staff, num_needed, invert=False
                            );
                    d.staff.extend(selected_staff);
                if len(selected_staff) != num_needed:
                    s.errors.append('Not enough eligible staff on day {0}.'.format(day))
            day += 1;

# record_staff_days records the scheduled days of each staff member in the
# object corresponding to each staff member.
def _record_staff_days(s):
    day = 0;
    for w in s.weeks:
        for d in w.days:
            for staff in d.staff:
                staff.daysScheduled.append(day);
            day += 1;

# weighted_select_n selects a subset of n elements from a lst of Staff objects.
# If invert is True then lower seniority staff are more likely to be selected
# (weekends).
# If invert is False then higher seniority staff are more likely to be selected
# (weekdays).
def _weighted_select_n(lst, n, invert=True):
    if invert:
        weights = _normalize_weights([1/el.seniority for el in lst]);
    else:
        weights = _normalize_weights([el.seniority for el in lst]);
    res = [];
    for i in range(n):
        chosen = _weighted_choice(lst, weights);
        res.append(chosen);
        # remove chosen from list and update weights
        lst.pop(lst.index(chosen));
        if invert:
            weights = _normalize_weights([1/el.seniority for el in lst]);
        else:
            weights = _normalize_weights([el.seniority for el in lst]);
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

def _normalize_weights(lst):
    total_weight = sum(lst);
    return [el/total_weight for el in lst];

def _has_day_off(person, day):
    scheduled_off = (person.daysRequestedOff +
                    person.daysRequestedOffSchool + 
                    person.daysVacation)
    return (day in scheduled_off)
