def is_leap_year(year: int) -> bool:
    if year%400 == 0:
        return True
    elif year%4 == 0:
        if year%100 == 0:
            return False
        else:
            return True
    else:
        return False
