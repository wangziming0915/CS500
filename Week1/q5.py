print("This program calculats the CD of months")

initialDep = int(input("Enter the initial deposit amount: "))
annualPerY = float(input("Enter annual percentage yield: "))
numberOfMonths = int(input("Enter maturity period(number of months): "))

print("The CD Calculator")

for i in range(numberOfMonths):
    initialDep += initialDep * annualPerY / 1200
    print(str(i + 1) + " " + "$" + str(initialDep))