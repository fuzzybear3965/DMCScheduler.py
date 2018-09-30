import sys, abc

class Staff(abc.ABC):

    __id = 0;

    @abc.abstractmethod
    def __init__(self, fname, lname, seniority, daysRequestedOn,
            daysRequestedOff, daysRequestedOffSchool, daysVacation,
            daysEducation, daysBonus):

        self.first = fname;
        self.last = lname;
        self.seniority = seniority;

        self.daysRequestedOn = csv_list_to_python_list(daysRequestedOn);
        self.daysRequestedOff = csv_list_to_python_list(daysRequestedOff);
        self.daysRequestedOffSchool = csv_list_to_python_list(daysRequestedOffSchool);
        self.daysVacation = csv_list_to_python_list(daysVacation);
        self.daysEducation = csv_list_to_python_list(daysEducation);
        self.daysBonus = csv_list_to_python_list(daysBonus);

        print("Education days: {0}".format(self.daysEducation))

        # check to see if any days are defined in a conflicting way and throw an
        # error if any of the days overlap
        if common_elements([self.daysRequestedOn, self.daysRequestedOff,
            self.daysRequsetedOffSchool, self.daysVacation,
            self.daysEducation]):
            raise ValueError("Days not defined in unique ways for {0} {1}.".format(self.first, self.last))
        else:
            self.daysScheduled = list(set().union(self.daysRequestedOn, self.daysRequestedOff,
                self.daysRequestedOffSchool, self.daysVacation, self.daysEducation))

        # ensure that bonus days are requestedOn days
        if len(list(set().intersection(self.daysBonus,self.daysRequestedOn))) != len(self.daysBonus):
            raise ValueError("Not all bonus days were on a RequestedOn day for nurse {0} {1}".format(self.first, self.last))

        # made it here; increment ID
        self.__id = self.increment_id(); # increments the counter for the class
        
    @property
    def id(self):
        return self.__id


    @classmethod
    def increment_id(cls):
        cls.__id += 1;
        return cls.__id

    # From https://stackoverflow.com/questions/46851479/python-sort-list-with-two-arguments-in-compare-function
    def __lt__(self, other):
        s = self.first.lower() + self.last.lower()
        o = other.first.lower() + other.last.lower()
        return s < o

# n.id is an incremented value for each Nurse object that is instantiated
class Nurse(Staff):
    def __init__(self, fname, lname, seniority, isCharge, isVent,
            daysRequestedOn, daysRequestedOff, daysRequestedOffSchool,
            daysVacation, daysEducation, daysBonus):
        Staff.__init__(self, fname, lname, seniority, daysRequestedOn,
                daysRequestedOff, daysRequestedOffSchool, daysVacation,
                daysEducation, daysBonus)
        self.isCharge = True if isCharge.lower() == 'yes' else False;
        self.isVent = True if isCharge.lower() == 'yes' else False;

class CNA(Staff):
    def __init__(self, fname, lname, seniority, daysRequestedOn,
            daysRequestedOff, daysRequestedOffSchool, daysVacation,
            daysEducation, daysBonus):
        Staff.__init__(self, fname, lname, seniority, daysRequestedOn,
                daysRequestedOff, ddaysRequestedOffSchool, daysVacation)

def csv_list_to_python_list(CSVString):
    return list(map(lambda x: int(x), CSVString.split(','))) if CSVString != '' else []

def common_elements(lists):
    for i in range(len(lists)):
        for j in range(idx+1, len(lists)):
            common_elements = list(set(lists[i]).intersection(lists[j]))
            if common_elements:
                    return True
    return False
