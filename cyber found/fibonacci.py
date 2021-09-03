targetNum = int(input("Please enter a positive integer greater than 1: "))
count = 0
n1, n2 = 1, 1
while count != targetNum:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1
