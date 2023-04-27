import Expense
import csv

class Expense_repository:
    def __init__(self) -> None:
        self.__expenses = []

    def read_expense_file(self):
        with open('Expenses.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.__expenses.append(Expense(row[0], row[1], row[2], row[3]))

    def write_expense_file(self):
        with open('Expenses.csv', "wb") as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            for line in self.__expenses:
                writer.writerow(line)