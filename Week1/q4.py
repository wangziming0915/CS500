print("This program handles the checkout hotel room.")

ONE_PERSON_CHARGE = 155
TWO_PERSON_CHARGE = 160
THREE_PERSON_CHARGE = 165
TAX_RATE = 0.12

numberOfnights = int(input("Please input the number of nights: "))
numberOfPeople = int(input("Please enter the number of people: "))
mealCharges = int(input("Please enter the meal charges from the restaurant: "))

bill = 0

if numberOfnights < 1:
    print("Invalid input.")
elif numberOfPeople == 1:
    bill = (numberOfPeople * ONE_PERSON_CHARGE * numberOfnights + mealCharges) * (1 - TAX_RATE)
elif numberOfPeople == 2:
    bill = (numberOfPeople * TWO_PERSON_CHARGE * numberOfnights + mealCharges) * (1 - TAX_RATE)
else:
    bill = (numberOfPeople * THREE_PERSON_CHARGE * numberOfnights + mealCharges) * (1 - TAX_RATE)

print("The bill is: " + str(bill))