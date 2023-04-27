from random import *

randomNumber = randint(1, 20)
print("I am thinking of a number between 1 and 20.")
curInput = int(input("Can you guess what it is? "))
tryCounter = 0

while True:
    if(curInput > randomNumber):
        curInput = int(input("Your guess is high. Try again: "))
        tryCounter += 1
    elif(curInput < randomNumber):
        curInput = int(input("Your guess is low. Try again: "))
        tryCounter += 1
    else:
        print("Congratulations! You did it.")
        break
    if(tryCounter == 5):
        print("You should have gotten it by now.")
        print("Better luck next time.")
        break