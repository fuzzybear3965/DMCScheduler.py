import sys

class Nurse:
    first = '';
    last = '';
    isCharge = 0;
    seniority = -1;
    daysRequested = [];
    shiftsPerWeek = 3; # TODO: Change per nurse;
    RO = [];

    def __init__(self, fname, lname, isCharge, daysRequested, RO, seniority):
        self.first = fname;
        self.last = lname;
        self.isCharge = 1 if isCharge.lower() == 'yes' else 0;
        self.daysRequested = list(map(lambda x: int(x), daysRequested.split(',')));
        self.RO = list(map(lambda x: int(x), RO.split(','))) if RO != '' else []
        self.seniority = seniority;

# From https://stackoverflow.com/questions/46851479/python-sort-list-with-two-arguments-in-compare-function
    def __lt__(self, other):
        s = self.first.lower() + self.last.lower()
        o = other.first.lower() + other.last.lower()
        return s < o

class CNA:
    first = '';
    last = '';
    isCharge = 0;
    seniority = -1;
    daysRequested = [];
    shiftsPerWeek = 3; # TODO: Change per nurse;
    RO = [];

    def __init__(self, fname, lname, isCharge, daysRequested, RO, seniority):
        self.first = fname;
        self.last = lname;
        self.isCharge = 1 if isCharge.lower() == 'yes' else 0;
        self.daysRequested = list(map(lambda x: int(x), daysRequested.split(',')));
        self.RO = list(map(lambda x: int(x), RO.split(','))) if RO != '' else []
        self.seniority = seniority;

# From https://stackoverflow.com/questions/46851479/python-sort-list-with-two-arguments-in-compare-function
    def __lt__(self, other):
        s = self.first.lower() + self.last.lower()
        o = other.first.lower() + other.last.lower()
        return s < o
