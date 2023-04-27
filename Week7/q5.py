from abc import ABC, abstractclassmethod, abstractproperty
import enum

class Displayable(ABC):
    @abstractclassmethod
    def display():
        pass

class Flyable(ABC):
    @abstractclassmethod
    def fly():
        pass

class BuildingType(enum):
    HEAVY_INDUSTRIAL = 0
    WAREHOUSE = 1
    COULD_STORAGE = 2
    LIGHT_INDUSTRIAL = 3
    DATA_HOUSING = 4

class Product(Displayable):
    def __init__(self, product_name: str, base_price: float) -> None:
        self.__product_name = product_name
        self.__base_price = base_price

    @property
    def product_name(self) -> str:
        return self.__product_name

    @property
    def base_price(self) -> float:
        return self.__base_price

    def __iter__(self):
        self.a = -1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

    def get_final_price() -> float:
        pass


class Factory(Displayable):
    def __init__(self, factory_name: str, products:list[Product]) -> None:
        self.__factory_name = factory_name
        self.__products = products

    @property
    def factory_name(self) -> str:
        return self.__factory_name

    @property
    def products(self) -> str:
        return self.__products


    def add_product(self, product: Product):
        self.__products.append(product)

    def get_top_three_expensive_products(self) -> list[Product]:
        resultList = []
        prodMap = {}

        for product in self.products:
            prodMap[product.base_price] = product
        
        keys = list(prodMap.keys())
        keys.sort()
        prodMap = {i: prodMap[i] for i in keys}

        for i in 3:
            resultList.append(prodMap[len(keys) - i + 1])

    def get_all_computers_with_touch_screen(self) -> list[Computer]:
        computerList = []
        for product in self.products:
            if isinstance(product, Computer):
                if product.touch:
                    computerList.append(product)
    
        return computerList

    def remove_all_computers(self, model: str):
       for product in self.products:
            if isinstance(product, Computer):
                if product.model == model:
                    self.products.remove(product)

    def display(self):
        pass


class Building(Displayable):
    def __init__(self, building_name: str, area: float, stories: int, type: int):
        self.__building_name = building_name
        self.__area = area
        self.__stories = stories
        self.__type = BuildingType[type]
    
    @property
    def building_name(self) -> str:
        return self.__building_name

    @property
    def area(self) -> float:
        return self.__area

    @property
    def stories(self) -> int:
        return self.__stories

    @property
    def type(self) -> BuildingType:
        return self.__type

    def display(self):
        print(f"The building name is {self.building_name}, area is {self.area}, stories is {self.stories}, type is {self.type}")




class ProductFactory(Factory):
    def __init__(self, factory_name: str, products: list[Product], category: str, buildings: list[Building]):
        super().__init__(factory_name, products)
        self.__category = category
        self.__buildings = buildings

    @property
    def category(self) -> str:
        return self.__category

    @property
    def buildings(self) -> list[Building]:
        return self.__buildings   


class Computer(Product):
    def __init__(self, product_name: str, base_price: float, model: str, speed: float, touch: bool, cellular: bool) -> None:
        super().__init__(product_name, base_price)
        self.__model = model
        self.__speed = speed
        self.__touch = touch
        self.__cellular = cellular

    @property
    def model(self) -> str:
        return self.__model

    @property
    def speed(self) -> float:
        return self.__speed 

    @property
    def touch(self) -> bool:
        return self.__touch 

    @property
    def cellular(self) -> bool:
        return self.__cellular     

    def get_final_price(self) -> float:
        price = self.base_price
        touchFee = price * 0.2
        cellularFee = price * 0.15
        if self.touch:
            price += touchFee
        if self.cellular:
            price += cellularFee
        
        return price

    def compute(self):
        print("compute")

    def display(self):
        print(f"The product name is {self.product_name}, base price is {self.base_price}, model is {self.model}, speed is {self.speed}, touch is {self.touch}, cellular is {self.cellular}.")

class Drone(Product, Flyable):
    def __init__(self, product_name: str, base_price: float, camera: str, max_flight_time: float, gps: bool) -> None:
        Product().__init__(product_name, base_price)
        self.__camera = camera
        self.__max_flight_time = max_flight_time
        self.__gps = gps

    @property
    def camera(self) -> str:
        return self.__camera

    @property
    def max_flight_time(self) -> float:
        return self.__max_flight_time

    @property
    def gps(self) -> bool:
        return self.__gps

    def get_final_price(self) -> float:
        if self.gps:
            return self.base_price * 1.15
        else:
            return self.base_price

    def display(self):
        print(f"The product name is {self.product_name}, base_price is {self.base_price}, camera is {self.camera}, max_flight_time is {self.max_flight_time}, gps is {self.gps}.")

    def fly(self):
        print("Flys")

    def record(self):
        print("Records")


def main():
    Computer1 = Computer("Computer1", 3000, "intel3", 500, True, True)
    Computer2 = Computer("Computer2", 4000, "intel4", 400, False, True)
    Computer3 = Computer("Computer3", 5000, "intel5", 700, True, False)
    Computer4 = Computer("Computer4", 6000, "intel6", 800, False, False)
    productFactory = ProductFactory("factory1", [Computer1, Computer2, Computer3, Computer4], "it", )

if __name__ == "__main__":
    main()