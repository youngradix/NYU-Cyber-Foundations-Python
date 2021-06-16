numberIn = int(input("Please enter a positve integer: "))
num = 0

for i in range(0, numberIn-2):
    num = num + 2
    print(num)
    if num >= numberIn-2:
        break
