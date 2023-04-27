print("This program calculates the net pay, gross pay and taxes for two employees")
PAY_RATE = 14.5
NUM_EMPLOYEES = 2
TAX_RATE = 0.20
REGULAR_HOURS = 40

for i in range(NUM_EMPLOYEES):
    workHours = int(input("Enter the number of work hours for employee " + str(i + 1) + ": "))

    if workHours <= 40:
        grossPay = workHours * PAY_RATE
    elif workHours <= 45:
        grossPay = 40 * PAY_RATE + (workHours - 40) * PAY_RATE * 1.5
    else:
        grossPay = 40 * PAY_RATE + 5 * PAY_RATE * 1.5 + (workHours - 45) * PAY_RATE * 2

    print("Employee " + str(i + 1) + ": ")
    print("The gross pay is: " + str(grossPay))
    print("The taxes are: " + str(grossPay * TAX_RATE))
    print("The net pay is: " + str(grossPay * (1 - TAX_RATE)))