

def check_year_leap(year):
    # check type
    if type(year) is int:
        if ((year % 4) == 0) and (((year % 100) != 0) or ((year % 400) == 0)):
            result = True
        else:
            result = False
    else:
        result = "Wrong Input"
    return result
