from tabulate import tabulate
print("This program surveys the opinions for 4 foods from students.")
print("For all opsions enter 1 for like, 2 for dislike.")
counterSet = [["Pizza", 0, 0], ["Hot Dog", 0, 0], ["Ham", 0, 0], ["Cheese", 0, 0]]

while True:
    pizza = input("Do you like Pizza? 1. Yes 2. No ")
    if(pizza == "1"):
        counterSet[0][1] += 1
    else:
        counterSet[0][2] += 1
    
    hotDog = input("Do you like Hot Dog? 1. Yes 2. No ")
    if(hotDog == "1"):
        counterSet[1][1] += 1
    else:
        counterSet[1][2] += 1

    ham = input("Do you like Ham? 1. Yes 2. No ")
    if(ham == "1"):
        counterSet[2][1] += 1
    else:
        counterSet[2][2] += 1

    cheese = input("Do you like Cheese? 1. Yes 2. No ")
    if(cheese == "1"):
        counterSet[3][1] += 1
    else:
        counterSet[3][2] += 1
    df = tabulate(counterSet, headers = [ 'Like', 'Dislike'], tablefmt ='orgtbl')
    print(df)
