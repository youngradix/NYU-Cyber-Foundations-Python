print("Please enter the number of coins: ")

quarters = int(input("# of quarters: "))
dimes = int(input("# of dimes: "))
nickels = int(input("# of nickels: "))
pennies = int(input("# of pennies: "))
quarters = quarters * 0.25

dimes = dimes * 0.10
nickels = nickels * 0.05
pennies = pennies * 0.01
total = quarters + dimes + nickels + pennies
total = str(total)
dollars = total[0]
cents = total[2:4]
print('The total is', dollars, 'dollars and', cents, 'cents.')
