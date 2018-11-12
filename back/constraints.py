# This file documents and stores many of the common constraints that would be
# used in a typical nursing schedule context.

MINSTAFFSIZE = 3  # TODO: Move constant to external source, like YAML/txt.

# TODO: Consider making this function depend on the day of the week, so is an
# array of minimum staff sizes for each day of the week.


def min_staff_size():
    return MINSTAFFSIZE


def penalty_shifts_per_week(nurse):
    if nurse.daysOn > nurse.shiftsPerWeek:
        return 1000
    return 0


def penalty_requested_off(day, day_idx):
    penalty = 0
    for nurse in day:
        nurse.RO.index(day_idx)
        print('Nurse {0} {1} requested {2} off and did not receive it.'.format(nurse.first, nurse.last, day_idx))
        penalty += 1  # penalty of 1
    return penalty
