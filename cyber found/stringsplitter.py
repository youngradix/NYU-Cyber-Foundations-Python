stdIn = input("Enter an odd length string: ")
stringSize = len(stdIn)
middleIndex = int((len(stdIn)-1)/2)
middleChar = stdIn[middleIndex]
print("Middle character: ", middleChar)
firstHalf = stdIn[:middleIndex]
print("First half: ", firstHalf)
secondHalf = stdIn[middleIndex + 1:]
print("Second half: ", secondHalf)