print("This program sums a sequence of product prices.")

priceList = input("Enter a list of prices: ")
priceList = priceList.split(" ")
print(priceList)

sum = 0

for i in range(1, len(priceList)):
    price = float(priceList[i])
    sum += price

print("The sum is $" + str(sum))