from bank import Bank
from customer import Customer

class BankApp:
    def __init__(self) -> None:
        self.__bank = Bank("SFBU Bank")

    def show_menu(self):
        print("Menu")
        print("1. Add a customer")
        print("2. Print all customers forward")
        print("3. Print all customers backward")
        print("4. edit the client's information")
        print("5. remove the client record")
        print("6. print out a list of clients with last names that match a user-specified last name")
        print("7. find the biggest and smallest account balance.")

        print("10. Exit")

    def get_user_choice(self) -> int:
        userInput = int(input("Enter the number for your option:"))
        return userInput

    def process_command(self, choice: int) -> None:
        if choice == 1:
            acc_number = int(input("Enter your account number:"))
            first_name = input("Enter your first name:")
            last_name = input("Enter your last name:")
            balance = float(input("Enter your account balance:"))

            customer = Customer(acc_number, first_name, last_name, balance)

            self.__bank.add_customer(customer)
            
        elif choice == 2:
            self.__bank.customers.sort(key= lambda x: x.acc_number)
            for customer in self.__bank.customers:
                print(customer.__str__())
        elif choice == 3:
            self.__bank.customers.sort(key= lambda x: x.acc_number, reverse = True)
            for customer in self.__bank.customers:
                print(customer.__str__())
        elif choice == 4:
            acc_number = int(input("Enter your new account number:"))
            first_name = input("Enter your new first name:")
            last_name = input("Enter your new last name:")
            balance = float(input("Enter your new account balance:"))

            customer = Customer(acc_number, first_name, last_name, balance)

            self.__bank.update_customer(customer)
        elif choice == 5:
            acc_number = int(input("Enter your account number:"))

            self.__bank.remove_customer(acc_number)
        elif choice == 6:
            last_name = input("Enter your new last name:")

            for customer in self.__bank.customers:
                if customer.__last_name == last_name:
                    print(customer.__str__())
        elif choice == 7:
            self.__bank.customers.sort(key= lambda x: x.__balance)

            print(f"The smallest balance is {self.__bank.__customers[0].__balance}")
            print(f"The highest balance is {self.__bank.__customers[len(self.__bank.__customers) - 1].__balance}")
        elif choice == 10:
            return
        else:
            print("Invalid input.")
            return



def main():
    app = BankApp()
    while True:
        app.show_menu()
        choice = app.get_user_choice()
        app.process_command(choice)

if __name__ == "__main__":
    main()