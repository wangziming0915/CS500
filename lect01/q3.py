def isPalindrom(inputStr):
    if(inputStr == inputStr[::-1]): 
        return True 
    else: 
        return False

def main():
    print("This program determines whether or not it is a palindrome.")
    curStr = input("Please enter a five-digit integer: ")
    if(len(curStr) != 5 or not curStr.isdigit()):
        print("Invalid input!")
    else:
        if(isPalindrom(curStr)):
            print("The 5-digit integer is palindrome.")
        else:
            print("The 5-digit integer is not palindrome.")

if __name__ == "__main__":
    main()
    