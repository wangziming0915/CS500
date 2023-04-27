from datetime import datetime, timedelta

class Department:
    def __init__(self, department_name) -> None:
        self.__department_name = department_name
        self.__employee_list = []
        self.__expense_list = []
    
    def add_employee(self, employee):
        if employee not in self.__employee_list:
            self.__employee_list.append(employee)
    
    def remove_employee(self, employee):
        if employee in self.__employee_list:
            self.__employee_list.remove(employee)
    
    def add_expense(self, expense):
        if expense not in self.__expense_list:
            self.__expense_list.append(expense)
    
    def remove_expense(self, expense):
        if expense in self.__expense_list:
            self.__expense_list.remove(expense)

    def report_expense(self, month: int)-> str:
        pass

    def __eq__(self, __value: object) -> bool:
        return isinstance(__value, Department) and __value.__department_name == self.__department_name