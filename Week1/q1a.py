print("This program sums a sequence of product prices.")

number_of_prices = int(input("Enter the number of prices: "))
sum_of_prices = 0
priceList = []

for i in range(1, number_of_prices + 1):
    sum_of_prices += float(input("Enter price " + str(i) + ": "))

print("The sum is $", sum_of_prices)