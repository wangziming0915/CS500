import csv
import Department

class Department_repository:
    def __init__(self) -> None:
        self.__departments = []

    def read_department_file(self):
        with open('Departments.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.__departments.append(Department(row[0], row[1], row[2]))

    def write_expense_file(self):
        with open('Departments.csv', "wb") as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            for line in self.__departments:
                writer.writerow(line)