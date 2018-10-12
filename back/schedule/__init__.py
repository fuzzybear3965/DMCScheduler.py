from collections import Sequence
class Schedule(Sequence):
    def __init__(self,ns):
        self.weeks = []; # array of week objects
        self.nurses = ns; # array of all nurses

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

    from ._gen_schedule import gen_schedule
