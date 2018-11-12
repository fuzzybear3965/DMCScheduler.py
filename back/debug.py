# Think of of making week an object (instead of a list of days), where the list
# of nurses used is one property. This will avoid the need to pass in the list
# of nurses separately


def print_week(week, ns):
    longest_name = ''
    for day in week:
        for nurse in day:
            name = nurse.first + ' ' + nurse.last
            if len(name) > len(longest_name):
                longest_name = name
    cell_width = 8
    # print('{:{width}}'.format('',width=cell_width),end='');  # header
    for i, day in enumerate(week):
        # Print 'Day 0     Day 1 ...' header
        print('{0:<{width}}'.format('Day ' + str(i), width=cell_width), end='')
    print()
    # Print days for nurse 1 through n
    for n in ns:
        cnt = 0  # number of days working
        for day in week:
            if n in day:
                cnt += 1
                print(2*' ' + '{0:<{width}}'.format('X', width=cell_width-2), end='')
            else:
                print('{:^{width}}'.format('', width=cell_width), end='')
        print(' | {0:<{width}}'.format(n.first + ' ' + n.last + ' (' + str(cnt) + ')', width=cell_width), end='')
        print()  # clear after
    print(6*cell_width*'-')
    for day in week:
        print(2*' '+'{0:<{width}}'.format(len(day), width=cell_width-2), end='')
    print()


def print_nurse(n):
    print("Name: {0} {1}, isCharge: {2}, daysOn = {3}".format(n.first, n.last, n.isCharge, n.daysOn))


def print_day(day):
    print()  # clear before
    for nurse in day:
        print_nurse(nurse)
    print()  # clear after
