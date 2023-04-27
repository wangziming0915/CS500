from tabulate import tabulate
employees = []

while True:
    print("e - Enter a new employee's information")
    print("a - Display all employees information")
    print("d - Display an employee's information")
    print("q - Quit")
    userInput = input("Please enter your option: ")
    if(userInput == "e"):
        employee = []
        name = input("Enter the name: ")
        employee.append(name)
        userId = input("Enter the ID: ")
        employee.append(userId)
        depNum = input("Enter the department number: ")
        employee.append(depNum)
        age = input("Enter the age of the employee: ")
        employee.append(age)
        employees.append(employee)
    elif(userInput == 'a'):
        df = tabulate(employees, headers = [ 'Name', 'ID', 'Department Number', 'Age'], tablefmt ='orgtbl')
        print(df)
    elif(userInput == 'd'):
        targetName = input("Enter the employee's name: ")
        for i in range(len(employees)):
            if(employees[i][0] == targetName):
                print(employees[i])
            else:
                print("The employee doesn't exist. Do you want to enter the new record?")
                userOption = input("YES or NO")
                if(userOption == "YES"):
                    employee = []
                    name = input("Enter the name: ")
                    employee.append(name)
                    userId = input("Enter the ID: ")
                    employee.append(userId)
                    depNum = input("Enter the department number: ")
                    employee.append(depNum)
                    age = input("Enter the age of the employee: ")
                    employee.append(age)
                    employees.append(employee)
    else:
        break



