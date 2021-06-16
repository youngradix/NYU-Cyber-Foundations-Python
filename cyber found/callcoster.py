days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

day=str(input("Enter the day the call started at: "))
startTime = int(input("Enter the time the call started at (hhmm): "))
duration = int(input("Enter the duration of the call (in minutes): "))

if day in days[0:5]:
    weekday = True
else:
    weekday = False

