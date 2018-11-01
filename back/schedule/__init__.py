from collections import Sequence
class Schedule(Sequence):
    def __init__(self,staff):
        self.weeks = []; # array of week objects
        self.staff = staff; # array of all staff members
        self.errors = [];

    def __str__(self):
        res = '';
        for w in self.weeks:
            res += str(w);
        return res

    def __repr__(self):
        return str(self);

    def __len__(self):
        return len(self.weeks)

    def __getitem__(self, indices):
        return self.weeks[indices]

    def json_representation(self):
        res = {};
        res['message'] = 'schedule';
        schedule = [];
        for n in self.staff:
            schedule.append({'name': n.first + ' ' + n.last});
            day = 0;
            for w in self.weeks:
                for d in w.days:
                    if n in d.staff:
                        cell_string = '';
                        if n.isCharge and not n.isVent:
                            cell_string = '7P(C)';
                        elif n.isCharge and n.isVent:
                            cell_string = '7P(C)(V)';
                        elif not n.isCharge and n.isVent:
                            cell_string = '7P(V)';
                        else:
                            cell_string = '7P';
                        if day in n.daysBonus:
                            cell_string += '$';
                        schedule[len(schedule)-1]['day'+str(day)] = cell_string
                    else:
                        schedule[len(schedule)-1]['day'+str(day)] = '';
                    day += 1;
        res['schedule'] = schedule;
        res['errors'] = self.errors;
        return res
            
    from ._gen_schedule import gen_schedule
    from ._check_schedule import check_schedule
