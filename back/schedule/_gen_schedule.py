from ._calendar import Week

def gen_schedule(self):
    init_schedule(self);
    cull_schedule(self);

# init_schedule adds nurses to those days they have requested
def init_schedule(self):
    self.weeks = [Week(self.nurses) for i in range(4)]
    
    # Add nurses to their requested days
    for n in self.nurses:
        for d in n.daysRequestedOn:
            week_idx = d // 7;
            day_idx = d % 7;
            self.weeks[week_idx].days[day_idx].nurses.append(n)

# cull_schedule removes nurses of low seniority from weekdays and high seniority
# from weekends. It brings the maximum number of nurses to the minimum required
# for all days. populate_schedule adds more nurses to certain days
def cull_schedule(self):
    for widx,w in enumerate(self.weeks):
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
