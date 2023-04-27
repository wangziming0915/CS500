#A
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

#B
class Button:
    def __init__(self) -> None:
        pass

class Shirt:
    def __init__(self) -> None:
        self.__Buttons = []

    def addButton(self):
        button = Button()
        self.__Buttons.append(button)

#C
class Chimney:
    def __init__(self) -> None:
        pass

class Kitchen:
    def __init__(self) -> None:
        self.Chimney = Chimney()

#D
#The relationship is Aggregation. Because the "components"'s life cycle will not end after the container object is collected. Also because the "components" is not initialized in the container class.

#E
#The relastionship is composition. It is because the components object is initialized inside the container class.