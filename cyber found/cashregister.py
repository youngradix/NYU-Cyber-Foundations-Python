item1Price = float(input("Enter price of the first item: "))
item2Price = float(input("Enter price of the second item: "))
clubCard = input("Does customer have a club card? Y/N: ")
taxRate = float(input("Enter tax rate, e.g. 5.5 for 5.5% tax: "))

basePrice = '%.2f' % round(item1Price + item2Price, 2)
print(f'base price = {basePrice}')

if (item1Price < item2Price) and (clubCard == "y" or clubCard == "Y"):
    item1Price = item1Price / 2
    newPrice = item1Price + item2Price
    newPrice = newPrice * 0.9
elif (item1Price < item2Price) and (clubCard == "n" or clubCard == "N"):
    item1Price = item1Price / 2
    newPrice = item1Price + item2Price
elif (item2Price < item1Price) and (clubCard == "y" or clubCard == "Y"):
    item2Price = item2Price / 2
    newPrice = item1Price + item2Price
    newPrice = newPrice * 0.9
else:
    item2Price = item2Price / 2
    newPrice = item1Price + item2Price

priceAfterDiscounts = '%.2f' % round(newPrice, 2)
priceAfterDiscounts = print(f'price after discounts = {priceAfterDiscounts}')

taxAmount = newPrice * (taxRate/100)
totalPrice = '%.2f' % round(newPrice + taxAmount, 2)
print(f'total price = {totalPrice}')