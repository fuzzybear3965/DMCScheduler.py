import sys, abc, warnings

class Staff(abc.ABC):

    __id = 0;

    def __init__(self, 
            fname, 
            lname, 
            seniority, 
            weekendType, 
            isCharge, 
            isVent,
            days):

        self.first = fname;
        self.last = lname;
        self.seniority = int(seniority);
        self.weekendType = weekendType;

        self.isCharge = True if isCharge == 'Yes' else False;
        self.isVent = True if isVent == 'Yes' else False;

# from https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-given-a-list-containing-it-in-python
        self.daysRequestedOn = [i for i,e in enumerate(days) if e == "7P"]
        self.daysRequestedOff = [i for i,e in enumerate(days) if e == "RO"]
        self.daysRequestedOffSchool = [i for i,e in enumerate(days) if e == "ROS"]
        self.daysVacation = [i for i,e in enumerate(days) if e == "VAC"]
        self.daysEducation = [i for i,e in enumerate(days) if e == "EDU"]
        self.daysBonus = [i for i,e in enumerate(days) if e == "7$P"]

        # check to see if any days are defined in a conflicting way and throw an
        # error if any of the days overlap
        # if has_common_elements([self.daysRequestedOn, self.daysRequestedOff,
            # self.daysRequestedOffSchool, self.daysVacation,
            # self.daysEducation]):
            # warnings.warn(("Days not defined in unique ways for {0} {1}.".format(self.first, self.last)))
        # else:
            # self.daysScheduled = list(set().union(self.daysRequestedOn, self.daysRequestedOff,
                # self.daysRequestedOffSchool, self.daysVacation, self.daysEducation))

        self.daysScheduled = [];
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

    def __str__(self):
        res = 'Name: {0} {1}\n'.format(self.first, self.last);
        res += 'Charge: {0}\n'.format('Yes' if self.isCharge else 'No')
        res += 'Vent: {0}\n'.format('Yes' if self.isVent else 'No')
        res += 'Seniority: ' + str(self.seniority) + '\n'
        res += 'Weekend Type: ' + str(self.weekendType) + '\n'
        res += 'Days Requested On: ' + ','.join(str(e) for e in self.daysRequestedOn) + '\n'
        res += 'Days Requested Off: ' + ','.join(str(e) for e in self.daysRequestedOff) + '\n'
        res += 'Days Requested Off School: ' + ','.join(str(e) for e in self.daysRequestedOffSchool) + '\n'
        res += 'Vacation Days: ' + ','.join(str(e) for e in self.daysVacation) + '\n'
        res += 'Education Days: ' + ','.join(str(e) for e in self.daysEducation) + '\n'
        res += 'Bonus Days: ' + ','.join(str(e) for e in self.daysBonus) + '\n'
        return res

def csv_list_to_python_list(CSVString):
    return list(map(lambda x: int(x), CSVString.split(','))) if CSVString != '' else []

# has_common_elements accepts a list of lists as an argument. The return is a
# boolean indicating whether any of the lists share any common elements.
def has_common_elements(lists):
    for i in range(len(lists)):
        for j in range(i+1, len(lists)):
            has_common_elements = list(set(lists[i]).intersection(lists[j]))
            if has_common_elements:
                    return True
    return False
