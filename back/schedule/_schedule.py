class Day:
    def __init__(self):
        self.staff = []  # array of Nurse objects
        self.cnas = []  # array of CNAs

    def __str__(self):
        res = ''
        for n in self.staff:
            res += ('{0} {1} (sen: {2})\n '.format(n.first, n.last, str(n.seniority)))
        return res


class Week:
    def __init__(self, ns):
        self._allstaff = ns  # array of staff
        self.days = [Day() for _ in range(7)]  # array of day objects

    def __str__(self):
        res = ''
        longest_name = ''
        for n in self._allstaff:
                name = n.first+' '+n.last
                if len(name) > len(longest_name):
                    longest_name = name
        cell_width = 8  #

        for i in range(len(self.days)):
            # Print 'Day 0     Day 1 ...' header
            res += '{0:<{width}}'.format('Day ' + str(i), width=cell_width)
        res += '\n'
        # Print header divider
        res += 7*cell_width*'-'
        res += '\n'
        # Print days for nurse 1 through n
        for n in self._allstaff:
            cnt = 0  # number of days working
            for day in self.days:
                if n in day.staff:
                    cnt += 1
                    res += 2*' ' + '{0:<{width}}'.format('X', width=cell_width-2)
                else:
                    res += '{:^{width}}'.format('', width=cell_width)
            res += ' | {0:<{width}}'.format(n.first + ' ' + n.last + ' (' + str(cnt) + ')', width=cell_width)
            res += '\n'
            # Print staff days divider
            res += 7*cell_width*'-'
            res += '\n'
        res += '\n'
        for day in self.days:
            res += 2*' '+'{0:<{width}}'.format(len(day.staff), width=cell_width-2)
        res += '\n'
        return res
