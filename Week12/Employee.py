class Employee:
    def __init__(self, employee_id, first_name, last_name, department_name, rank) -> None:
        self.__employee_id = employee_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__department_name = department_name
        self.__rank = rank

    def change_employee(self, employee_id, first_name, last_name, department_name, rank):
        self.__employee_id = employee_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__department_name = department_name
        self.__rank = rank

    def __eq__(self, __value: object) -> bool:
        return isinstance(__value, Employee) and __value.__employee_id == self.__employee_id

    def __str__(self) -> str:
        return (f"The employee id is {self.__employee_id}, first name is {self.__first_name}, last name is {self.__last_name}, department name is {self.__department_name}, rank is {self.__rank}")