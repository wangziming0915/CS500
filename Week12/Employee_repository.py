import Employee
import csv

class Employee_repository:
    def __init__(self) -> None:
        self.__employees = []

    def read_expense_file(self) -> list:
        with open('Departments.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.__employees.append(Employee(row[0], row[1], row[2], row[3]))
        return self.__employees

    def write_expense_file(self):
        with open('Employees.csv', "wb") as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            for line in self.__employees:
                writer.writerow(line)