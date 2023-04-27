class Account():
    def __init__(self, firstName: str, lastName: str, accNum: int, accBalance: int) -> None:
        self.__firstName = firstName
        self.__lastName = lastName
        self.__accNum = accNum
        self.__accBalance = accBalance

    @property
    def firstName(self) -> None:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str) -> None:
        self.__firstName = firstName

    @property
    def lastName(self) -> None:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str) -> None:
        self.__lastName = lastName

    @property
    def accNum(self) -> None:
        return self.__accNum

    @property
    def accBalance(self) -> None:
        return self.__accBalance

    @accBalance.setter
    def accBalance(self, accBalance: int) -> None:
        self.__accBalance = accBalance

    def getUserInfo(self) -> None:
        print(f"The first name is {self.__firstName}, the last name is {self.__lastName}, the account number is {self.__accNum}, the balance of the account is {self.__accBalance}")
        
class Bank():
    def __init__(self) -> None:
        self.listOfAcc = []
        self.dictionary = {}
    
    def addAcc(self, acc: Account):
        self.listOfAcc.append(acc)
        self.dictionary[acc.accNum] = acc

    def printPromt(self):
        print("Welcome to Dylan's APP.")
        print("1. Create a new account.")
        print("2. Display your account information.")
        print("3. Change your information.")
        print("4. Print all accounts backwards and forwards.")
        print()

    def processInput(self):
        userInput = int(input("Please enter the number for your option: "))
        if(userInput == 1):
            firstName = input("Please enter your first name: ")
            lastName = input("Please enter your last name: ")
            accNum = int(input("Please enter your account number: "))
            accBalance = int(input("Please enter your account balance: "))
            if(accountNum not in self.dictionary):
                newAcc: Account = Account(firstName, lastName, accNum, accBalance)
                self.addAcc(newAcc)
            else:
                print("Account number already used!")

        elif(userInput == 2):
            accountNum = int(input("Please enter your account number: "))
            if accountNum in self.dictionary:
                self.dictionary[accountNum].getUserInfo()

        elif(userInput == 3):
            accountNum = int(input("Please enter your account number: "))
            if accountNum in self.dictionary:
                account: Account = self.dictionary[accountNum]
                account.firstName = input("Please enter your first name: ")
                account.lastName = input("Please enter your last name: ")
                account.accBalance = int(input("Please enter your account balance: "))

        elif(userInput == 4):
            self.listOfAcc.sort(key=lambda x : x.accNum)
            for acc in self.listOfAcc:
                acc.getUserInfo()
            print()

            index = len(self.listOfAcc) - 1
            while(index >= 0):
                self.listOfAcc[index].getUserInfo()
                index -= 1


    def process(self):
        while True:
            self.printPromt()
            self.processInput()

    

def main():
    bank: Bank = Bank()
    bank.process()
    

if __name__ == "__main__":
    main()