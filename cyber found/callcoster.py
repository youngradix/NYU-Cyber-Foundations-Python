days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

day=str(input("Enter the day the call started at: "))
startTime = input("Enter the time the call started at (hhmm): ")
duration = int(input("Enter the duration of the call (in minutes): "))

if day in days[0:5]:
    weekday = True
else:
    weekday = False

if weekday == True and (startTime >= "0800" and startTime <= "1800"):
    rate = 0.40
    callCost = rate * duration
elif weekday == True and (startTime < "0800" or startTime > "1800"):
    rate = 0.25
    callCost = rate * duration
else:
    rate = 0.15
    callCost = rate * duration

callCost = '%2.f'.format(round(callCost, 2))
print(f'This call will cost ${callCost}')

