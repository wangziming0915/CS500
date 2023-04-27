class Tire:
    def __init__(self) -> None:
        pass

class Car:
    def __init__(self) -> None:
        self.__list_of_tires = []
    def addTire(self, tire: Tire):
        self.__list_of_tires.append(tire)
    def run(self):
        print("Run.")




