import math
from datetime import date

def easter_date_gauss(year: int) -> date:
    a = year%19
    b = year%4
    c = year%7
    p = math.floor(year/100)
    q = math.floor((13+8*p)/25)
    l = math.floor(p/4)

    m = (15+p-l-q) % 30
    n = (4+p-l) % 7

    d = (19*a+m) % 30
    e = (n+2*b+4*c+6*d) % 7

    day = d+e+22

    if d==29 and e==6 or \
       d==28 and e==6:
       day -= 7

    if day > 31:
        return date(year=year, month=4, day=day-31)
    else:
        return date(year=year, month=3, day=day)
