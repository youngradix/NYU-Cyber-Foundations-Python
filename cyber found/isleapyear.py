def isleapyear(year): 
    leapYear = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leapYear = True
                return leapYear 
            else:
                leapYear = False
                return leapYear
        else:
            leapYear = True    
            return leapYear        
    else:
        leapYear = False
        return leapYear

yearCheck = int(input("Please enter a year to check: "))
if isleapyear(yearCheck):
    print("Year {0} was a leapyear".format(yearCheck))