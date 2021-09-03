def max_val(lst):
    highestNum = 0
    for num in lst:
        if num > highestNum:
            highestNum = num
            return highestNum
    

print(max_val([-19, -3, 20, -1, 5, -25]))
