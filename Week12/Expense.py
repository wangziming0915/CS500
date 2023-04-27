class Expense:
    def __init__(self, date_of_expense, expense_amount, expense_category, employee_id) -> None:
        self.__date_of_expense = date_of_expense
        self.__expense_amount = expense_amount
        self.__expense_category = expense_category
        self.__employee_id = employee_id

    def change_Expense(self, date_of_expense, expense_amount, expense_category, employee_id) -> None:
        self.__date_of_expense = date_of_expense
        self.__expense_amount = expense_amount
        self.__expense_category = expense_category
        self.__employee_id = employee_id

    def __str__(self) -> str:
        return(f"The date of expense is {self.__date_of_expense}, the amount is {self.__expense_amount}, the category is {self.__expense_category}, the employee id is {self.__employee_id}")
    