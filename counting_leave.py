from datetime import timedelta


# Define the All Week Days to match the date.weekday function
(MON, TUE, WED, THU, FRI, SAT, SUN) = list(range(7))

# Define the Weekends to Subtract Leave Count from Given Date
weekends=(SAT,SUN)


def count_leave(from_date, to_date, holidays=[]):
    delta_days = (to_date - from_date).days + 1
    full_weeks, extra_days = divmod(delta_days, 7)
    # num_workdays = how many days/week you work * total # of weeks
    num_workdays = (full_weeks + 1) * (7 - len(weekends))
    # subtract out any working days that fall in the 'shortened week'
    for d in range(1, 8 - extra_days):
        if (to_date + timedelta(d)).weekday() not in weekends:
             num_workdays -= 1
    # skip holidays that fall on weekends
    holidays =  [x for x in holidays if x.weekday() not in weekends]
    # subtract out any holidays 
    for d in holidays:
        if from_date <= d <= to_date:
            num_workdays -= 1
    return num_workdays

def _in_between(a,b,x):
    return a <= x <= b or b <= x <= a

def cmp(a, b):
    return (a > b) - (a < b)

def count_workday(from_date, days=0, holidays=[]):
    if days== 0:
        return from_date;
    if days>0 and from_date.weekday() in weekends: #
      while from_date.weekday() in weekends:
          from_date -= timedelta(days=1)
    elif days < 0:
      while from_date.weekday() in weekends:
          from_date += timedelta(days=1)
    full_weeks, extra_days = divmod(days,7 - len(weekends))
    new_date = from_date + timedelta(weeks=full_weeks)
    for i in range(extra_days):
        new_date += timedelta(days=1)
        while new_date.weekday() in weekends:
            new_date += timedelta(days=1)
    # to account for days=0 case
    while new_date.weekday() in weekends:
        new_date += timedelta(days=1)

    # avoid this if no holidays
    if holidays:
        delta = timedelta(days=1 * cmp(days,0))
        # skip holidays that fall on weekends
        holidays =  [x for x in holidays if x.weekday() not in weekends ]
        holidays =  [x for x in holidays if x != from_date ]
        for d in sorted(holidays, reverse = (days < 0)):
            # if d in between start and current push it out one working day
            if _in_between(from_date, new_date, d):
                new_date += delta
                while new_date.weekday() in weekends:
                    new_date += delta
    return new_date

