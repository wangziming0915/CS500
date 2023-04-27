class Department:
    def __init__(self, department_name: str) -> None:
        self.__department_name = department_name
        self.__goods = []
    
    @property
    def department_name(self) -> str:
        return self.__department_name

    @property
    def goods(self) -> dict:
        return self.__goods


    def display(self):
        print(f"Department Partname Price Quantity available Quantity sold")
        print(f"Department {self.department_name}:")
        for good in self.goods:
            good.display()


class Parts:
    def __init__(self, partname: str, price: int, quantity_available: int, quantity_sold: int) -> None:
        self.__partname = partname
        self.__price = price
        self.__quantity_available = quantity_available
        self.__quantity_sold = quantity_sold
    
    @property
    def partname(self) -> str:
        return self.__partname
    
    @property
    def price(self) -> float:
        return self.__price

    @property
    def quantity_available(self) -> int:
        return self.__quantity_available

    @property
    def quantity_sold(self) -> int:
        return self.__quantity_sold

    def display(self):
        print(f"{self.partname}  {self.price}  {self.quantity_available}  {self.quantity_sold}")

class Store:
    def __init__(self) -> None:
        self.__departments = []

    @property
    def departments(self) -> list[Department]:
        return self.__departments

    @departments.setter
    def departments(self):
        self.departments = []


    def get_total_value_of_dept(self, department_name: str) -> dict:
        target_dept = 0
        mapping = {}

        for department in self.departments:
            if department.department_name == department_name:
                target_dept = department
        
        for part in target_dept.goods:
            mapping[part.partname] = part.price * part.quantity_available

        return mapping

    def get_total_value_of_store(self) -> dict[str, float]:
        mapping = {}

        for department in self.departments:
            total_value = 0
            for part in department.goods:
                total_value += part.price * part.quantity_available
            mapping[department.department_name] = total_value

        return mapping
        
    def get_highest_value_item(self) -> dict[str, str]:
        mapping = {}

        for department in self.departments:
            max_price_item = department.goods[0]
            for part in department.goods:
                if part.price > max_price_item.price:
                    max_price_item = part
            mapping[department.department_name] = max_price_item.partname

        return mapping

    def get_most_popular_item(self) -> tuple[str, str, int]:
        result = tuple("a","a",0)
        highest_sold = 0
        
        for department in self.departments:
            for part in department.goods:
                if part.quantity_sold > highest_sold:
                    result = (department.department_name, part.partname, part.quantity_sold)
                    highest_sold = part.quantity_sold

        return result

    def get_most_profitable_item(self) ->tuple[str, str, int]:
        result = tuple("a","a",0)
        highest_profit = 0
        
        for department in self.departments:
            for part in department.goods:
                if part.quantity_sold * part.price > highest_profit:
                    result = (department.department_name, part.partname, part.quantity_sold * part.price)
                    highest_profit = part.quantity_sold * part.price

        return result

    def __str__(self) -> str:
        for department in self.departments:
            department.display()


def main():
    store1 = Store()
    department1 = Department("Electronics")
    department2 = Department("Clothing ")
    department3 = Department("Hardware")
    part1 = Parts("Smartphone", 600, 1000, 2000)
    part2 = Parts("Tablet ", 500, 2500, 300)
    part3 = Parts("Monitor", 560, 1500, 200)
    department1.goods.append(part1)
    department1.goods.append(part2)
    department1.goods.append(part3)
    part4 = Parts("Pants", 50, 3000, 500)
    part5 = Parts("Coat", 150, 560, 10)
    department2.goods.append(part4)
    department2.goods.append(part5)
    part6 = Parts("Hammer", 30, 750, 60)
    part7 = Parts("Cabinet", 450, 600, 70)
    department3.goods.append(part6)
    department3.goods.append(part7)
    store1.departments.append(department1)
    store1.departments.append(department2)
    store1.departments.append(department3)

    print(f"{store1.get_highest_value_item()}")
    print(f"{store1.get_total_value_of_store()}")
    print(f"{store1.get_highest_value_item()}")
    print(str(store1.get_most_popular_item()))

    store1.__str__()


if __name__ == "__main__":
    main()
                

        
