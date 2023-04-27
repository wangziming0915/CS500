def showMenu():
    print("1. Find the smallest score")
    print("2. Find the largest score")
    print("3. Find the sum")
    print("4. Find the average score")
    print("5. Find the mode score")
    print("6. Exit")


def getData():
    scores = input("Please enter a list of scores separeted by space: ")
    scoresListStr = scores.split(" ")
    scoreList = []

    for score in scoresListStr:
        scoreList.append(int(score))
    
    return scoreList


def findTheSmallest(scoreList):
    minScore = float('inf')

    for i in range(len(scoreList)):
        if(scoreList[i] < minScore):
            minScore = scoreList[i]

    return minScore


def findTheLargest(scoreList):
    maxiumScore = float('-inf')
    for i in range(len(scoreList)):
        if(scoreList[i] > maxiumScore):
            maxiumScore = scoreList[i]

    return maxiumScore


def sumScore(scoreList):
    sum = 0
    for i in range(len(scoreList)):
        sum += scoreList[i]
    return sum


def findTheAverage(scoreList):
    averageScore = sumScore(scoreList) / len(scoreList)
    return averageScore


def findTheMode(scoreList):
    maxcount = 0
    element_having_max_freq = 0
    for i in range(0, len(scoreList)):
        count = 0
        for j in range(0, len(scoreList)):
            if(scoreList[i] == scoreList[j]):
                count += 1
            if(count > maxcount):
                maxcount = count
                element_having_max_freq = scoreList[i]
    
    return element_having_max_freq
    


def main():
    print("Finding the smallest, largest, sum, average or mode from a list of scores")

    scoreList = getData()

    while True:
        showMenu()
        choice = int(input("Enter your choice: "))
        if(0 > choice or choice > 6):
            print("Invalid input.")
        if choice == 6:
            print("Bye.")
            break
        elif(choice == 1):
            print("The smallest score is: " + str(findTheSmallest(scoreList)))
        elif(choice == 2):
            print("The largest score is: " + str(findTheLargest(scoreList)))
        elif(choice == 3):
            print("The sum of the score list is: " + str(sumScore(scoreList)))
        elif(choice == 4):
            print("The average of the score list is: " + str(findTheAverage(scoreList)))
        elif(choice == 5):
            print("The mode of the score list is: " + str(findTheMode(scoreList)))


if __name__ == '__main__':
    main()