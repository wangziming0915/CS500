from abc import ABC, abstractclassmethod, abstractproperty

class Displayable(ABC):
    @abstractclassmethod
    def display():
        pass

class AbstracCompany(ABC):
    _max_num_employees = 10
    def get_employee_name_list() -> list[str]:
        pass
        

class Employee(Displayable):
    def __init__(self, empId: int, name: str, salary: float, title: str) -> None:
        self.__empId = empId
        self.__name = name
        self.__salary = salary
        self.__title = title
    
    @property
    def empId(self) -> int:
        return self.__empId

    @property
    def name(self) -> str:
        return self.__name

    @property
    def salary(self) -> float:
        return self.__salary

    @property
    def title(self) -> str:
        return self.__title

class Company(AbstracCompany):
    def __init__(self, comp_name: str) -> None:
        self.__comp_name = comp_name
        self.__employees = []
        self.__curIndex = 0
    
    @property
    def comp_name(self) -> str:
        return self.__comp_name

    @property
    def employees(self) -> list[Employee]:
        return self.__employees

    def get_employee_name_list(self) -> list[str]:
        name_list: list[str] = []
        for employee in self.__employees:
            name_list.append(employee.name)

        return name_list

    def add_employee(self, employee: Employee):
        if len(super().get_employee_name_list()) < super()._max_num_employees:
            self.__employees.append(employee)
        else:
            print("The employee list is full!")
    
    def remove_employee(self, empId: int):
        for employee in self.__employees:
            if employee.empId == empId:
                self.__employees.remove(employee)

    def update_employee_title(self, empId: int, title: str):
        for employee in self.__employees:
            if employee.empId == empId:
                employee.title = title

    def remove_all_employees_by_title(self, title: str):
        for employee in self.__employees:
            if employee.title == title:
                self.__employees.remove(employee)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.employees:
            raise StopIteration

        if self.__curIndex < len(self.employees):
            employee = self.employees[self.__curIndex]
            self.__curIndex += 1
            return employee

        raise StopIteration

class StockBusiness(Displayable):
    def __init__(self, research_tool: str, commission_rate: float) -> None:
        self.__research_tool = research_tool
        self.__commission_rate = commission_rate

    @property
    def research_tool(self) -> str:
        return self.__research_tool

    @property
    def commission_rate(self) -> float:
        return self.__commission_rate  

    def trade(self, stock_name: str, num_shares: int):
        print(f"Trading {stock_name} {num_shares} shares.")

class TradingCompany(Company, StockBusiness):
    def __init__(self, comp_name: str, research_tool: str, commission_rate: float, product_type: str, num_of_offices: int) -> None:
        Company().__init__(self, comp_name)
        StockBusiness().__init__(self, research_tool, commission_rate)
        self.__product_type = product_type
        self.__num_of_offices = num_of_offices

    @property
    def product_type(self) -> str:
        return self.__product_type

    @property
    def num_of_offices(self) -> int:
        return self.__num_of_offices

    def get_employee_high_salary(self, limit: float) -> list[Employee]:
        empList = []
        for employee in super().employees:
            if employee.salary >= limit:
                empList.append(employee)

        return empList

    def get_employees_by_title(self) -> dict[str, list[str]]:
        dictionary = {}
        for employee in super().employees:
            if employee.title in dictionary:
                dictionary[employee.title].append(employee)
            else:
                dictionary[employee.title] = [employee]
        
        return dictionary

def main():
    Apple = Company("Apple")
    Chase = TradingCompany("Chase", "xxx", 20.0, "bank", 200)
    employee1 = Employee(111, "Dylan", 5000, "Officer")
    employee2 = Employee(222, "Jack", 6000, "Manager")
    Apple.add_employee(employee1)
    Apple.add_employee(employee2)

if __name__ == "__main__":
    main()


