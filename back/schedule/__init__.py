from collections import Sequence
class Schedule(Sequence):
    def __init__(self,staff):
        self.weeks = []; # array of week objects
        self.staff = staff; # array of all staff members

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
        res = [];
        for n in self.staff:
            res.append({'name': n.first + ' ' + n.last})
            day_cnt = 0;
            for w in self.weeks:
                for d in w.days:
                    if n in d.staff:
                        res[len(res)-1]['day'+str(day_cnt)] = '7PC'
                    else:
                        res[len(res)-1]['day'+str(day_cnt)] = ''
                    day_cnt += 1;
        return res

    from ._gen_schedule import gen_schedule
