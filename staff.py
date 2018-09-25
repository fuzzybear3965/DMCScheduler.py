import sys, abc

class Staff(abc.ABC):

    __id = 0;

    @abc.abstractmethod
    def __init__(self,fname, lname, daysRequested, daysVAC, daysRO, seniority=-1):
        self.first = fname;
        self.last = lname;

        self.daysRequested = list(map(lambda x: int(x), daysRequested.split(',')));
        self.daysVAC = list(map(lambda x: int(x), daysVAC.split(','))) if daysVAC != '' else [];
        self.daysRO = list(map(lambda x: int(x), daysRO.split(','))) if daysRO != '' else []

        self.seniority = seniority;

        self.__id = self.incrementID(); # increments the counter for the class
        self.daysScheduled = [];

    @property
    def id(self):
        return self.__id


    @classmethod
    def incrementID(cls):
        cls.__id += 1;
        return cls.__id

    # From https://stackoverflow.com/questions/46851479/python-sort-list-with-two-arguments-in-compare-function
    def __lt__(self, other):
        s = self.first.lower() + self.last.lower()
        o = other.first.lower() + other.last.lower()
        return s < o

# n.id is an incremented value for each Nurse object that is instantiated
class Nurse(Staff):
    def __init__(self, fname, lname, daysRequested, daysRO, daysVAC, seniority, isCharge, isVent):
        Staff.__init__(self,fname, lname, daysRequested, daysVAC, daysRO, seniority)
        self.isCharge = True if isCharge.lower() == 'yes' else False;
        self.isVent = True if isCharge.lower() == 'yes' else False;

class CNA(Staff):
    def __init__(self, fname, lname, daysRequested, daysVAC, daysRO, seniority):
        Staff.__init__(self,fname, lname, daysRequested, daysVAC, daysRO, seniority)
