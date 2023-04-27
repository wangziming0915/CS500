capitalList = [["china", "beijing"],["germany", "berlin"],["thailand", "bangkok"],["japan", "tokyo"],["united States", "washington, d.c"]]
correctCounter = 0

for i in range(len(capitalList)):
    userInput = input("What is the capital of " + capitalList[i][0] + "? ")
    if(userInput.lower() == capitalList[i][1]):
        print("Your answer is correct")
        correctCounter += 1
    else:
        print("The correct answer should be " + capitalList[i][1])

print("The correct count is " + str(correctCounter))