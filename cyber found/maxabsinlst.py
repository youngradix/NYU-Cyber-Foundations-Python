def max_abs_val(lst):
    maxAbs = 0
    for num in lst:
        if abs(num) > maxAbs:
            maxAbs = num
            return maxAbs

print(max_abs_val([-19, -3, 20, -1, 0, -25]))