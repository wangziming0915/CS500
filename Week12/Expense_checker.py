import Employee

class Expense_checker:
    def __init__(self) -> None:
        self.__departments = []
    
    def create_employee(self, employee_id, first_name, last_name, department_name, rank) -> Employee:
        employee = Employee(employee_id, first_name, last_name, department_name, rank)
        return employee
    
    
