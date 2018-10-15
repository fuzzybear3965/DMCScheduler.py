from ._calendar import Week

def gen_schedule(self):
    _init_schedule(self);
    _cull_schedule(self);
    _populate_schedule(self);

# init_schedule adds nurses to those days they have requested
def _init_schedule(schedule):
    schedule.weeks = [Week(schedule.nurses) for i in range(4)]
    # Add nurses to their requested days
    for n in schedule.nurses:
        for d in n.daysRequestedOn:
            week_idx = d // 7;
            day_idx = d % 7;
            schedule.weeks[week_idx].days[day_idx].nurses.append(n)

# cull_schedule removes nurses of low seniority from weekdays and high seniority
# from weekends. It brings the maximum number of nurses to the minimum required
# for all days. populate_schedule adds more nurses to certain days
def _cull_schedule(schedule):
    for widx,w in enumerate(schedule.weeks):
        for didx, d in enumerate(w.days):
            # TODO: Make number of staff per day something user-configurable
            if len(d.nurses) > 7:
                # arrange nurses by seniority
                seniorities = [x.seniority for x in d.nurses]
                # taken from https://stackoverflow.com/questions/6618515/sorting-list-based-on-values-from-another-list
                d.nurses = [x for _,x in sorted(zip(seniorities, d.nurses), key=lambda pair: pair[0])]
                # too many weekend people, keep the low seniority folk
                if didx % 7 in (1,5):
                    d.nurses = d.nurses[0:7]
                else:
                    d.nurses = d.nurses[-7:]

# pop_schedule adds random eligible nurses of high seniority to understaffed
# weekdays and random eligible nurses of low seniority to understaffed weekends.
# Mondays and Fridays receive a random number of extra nurses to compensate for
# frequent sick days
def _populate_schedule(schedule):
    for widx, w in enumerate(schedule.weeks):
        for didx, d in enumerate(w.days):
            if len(d) < 7:
                if didx in (1,5): # monday/friday
                    print("{0} of week {1} is understaffed with {2} staff members.".format(didx, widx, len(d)))
                else:
                    print("{0} of week {1} is understaffed with {2} staff members.".format(didx, widx, len(d)))
