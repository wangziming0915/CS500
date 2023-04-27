print("This program reads and prints the input words in the same order.")
wordList = []
wordSet = set()

def main():
    while(True):
        curWord = input("Please enter the word: ")
        if(curWord == 'exit'):
            break
        else:
            if(curWord not in wordSet):
                wordList.append(curWord)
                wordSet.add(curWord)

    print(wordList)

if __name__ == '__main__':
    main()
