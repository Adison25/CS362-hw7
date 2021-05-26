def year(year):
    if year % 4 != 0:
        return "No"
    elif year % 100 == 0:
        return "Yes"
    elif year % 400 != 0:
        return "No"
    else:   
        return "Yes"