dollars = int(input("# of dollars: "))
dollars = float(dollars)
cents = int(input("# of cents: "))
cents = float(cents/100)
total = dollars + cents

quarters = int(total/0.25)
#print("Q: ", quarters)
totalAfterQ = round(total - (quarters * 0.25), 2)
#print("tAQ: ", totalAfterQ)

dimes = int(totalAfterQ/0.10)
#print("D: ", dimes)
totalAfterQD = round(totalAfterQ - (dimes * 0.10), 2)
#print("tAQD: ", totalAfterQD)

nickels = int(totalAfterQD/0.05)
#print("N: ", nickels)
totalAfterQDN = round(totalAfterQD - (nickels * 0.05), 2)
#print("tAQDN: ", totalAfterQDN)

pennies = int(totalAfterQDN/0.01)
#print("P: ", pennies)
totalAfterQDNP = round(totalAfterQDN - (pennies * 0.01), 2)
#print("tAQDNP: ", totalAfterQDNP)

print("The coins are %d quarters, %d dimes, %d nickels and %d pennies" % (quarters, dimes, nickels, pennies))