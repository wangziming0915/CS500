from abc import ABC, abstractclassmethod, abstractproperty

class Displayable(ABC):
    @abstractclassmethod
    def display(self) -> None:
        pass

class Flyable(ABC):
    @abstractclassmethod
    def fly(self) -> None:
        pass

class Movable(ABC):
    @abstractclassmethod
    def move(self) -> None:
        pass

class Part(Displayable):
    def __init__(self, partno: str, price: float) -> None:
        self.__partno = partno
        self.__price = price

    @property
    def partno(self) -> int:
        return self.__partno

    @property
    def price(self) -> float:
        return self.__price

    def __str__(self) -> str:
        return f"partno = {self.__partno}\nPrice = {self.__price}"

    def display(self) -> None:
        print(self)

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Part):
            return self.__partno == __o.__partno
        else:
            return False


class MovablePart(Movable, Part):
    def __init__(self, partno: int, price: int, type: str) -> None:
        Movable.__init__(self)
        Part.__init__(self, partno, price)
        self.__type = type

    @property
    def type(self) -> str:
        return self.__type

    def display(self) -> None:
        super().display()
        print(f"type = {self.type}")

    def move(self):
        print(f"partno: {super().partno} is moving fast!")


class Machine(Displayable):
    def __init__(self, machine_name: str) -> None:
        self.__machine_name = machine_name
        self.__parts: list[Part] = []

    @property
    def machine_name(self) -> str:
        return self.__machine_name

    @property
    def parts(self) -> list[Part]:
        return self.__parts

    @abstractclassmethod
    def dowork(self) -> None:
        pass

    def add_part(self, part: Part):
        self.__parts.append(part)

    def remove_part(self, partno: str):
        target_part: Part = Part(partno, 0)
        self.__parts.remove(target_part)

    def remove_padas(self, partno: str):
        target_index = -1
        for i in range(len(self.__parts)):
            if self.__parts[i].partno == partno:
                target_index = i
                break

        if target_index != -1:
            self.__parts.pop(target_index)

    def find_duplicated_parts(self) -> dict[int, int]:
        part_freq: dict[int, int] = {}

        for part in self.__parts:
            if part.partno in part_freq:
                part_freq[part.partno] += 1
            else:
                part_freq[part.partno] = 1

        partDic = {}
        for key in part_freq:
            if part_freq[key] > 1:
                partDic[key] = part_freq[key]

        return partDic

    def getMovableParts(self) -> list[Part]:
        partList: list[Part] = []
        for part in super().parts:
            if isinstance(part, MovablePart):
                partList.append(part)

        return partList


class JetFighter(Flyable):
    def __init__(self, model: str, speed: int) -> None:
        super().__init__()
        self.__model = model
        self.__speed = speed

    @property
    def model(self) -> str:
        return self.__model

    @property
    def speed(self) -> int:
        return self.__speed

    def fly(self):
        print(f"The JetFighter {self.__model} is flying in the sky!")

    def display(self):
        print(f"The model is {self.__model}, the speed is {self.__speed}.")


class Robot(Machine, JetFighter):
    def __init__(self, machine_name: str, cpu: str, model: str, speed: int) -> None:
        Machine.__init__(self, machine_name)
        JetFighter.__init__(self, model, speed)
        self.__cpu = cpu
        self.__curIndex = 0

    @property
    def cpu(self) -> str:
        return self.__cpu

    def dowork(self):
        print(f"The Robot {super().machine_name} is assembling a big truck.")

    def fly(self):
        JetFighter.fly(self)
        print(f"The Robot {super().machine_name} is flying over the ocean!")

    def display(self):
        print(f"cpu = {self.__cpu}\nmachine_name = {super().machine_name}")
        print(f"The machine has these parts:")
        for part in super().parts:
            part.display()
            print()
        print(f"model = {super().model}\nspeed = {super().speed}")


    def get_expensive_parts(self, price_limit) -> list[Part]:
        partList: list[Part] = []
        for part in super().parts:
            if part.partno >= price_limit:
                partList.append(part)
        
        return partList

    def get_movable_parts(self) -> list[Part]:
        partList: list[Part] = []
        for part in super().parts:
            if isinstance(part, MovablePart):
                partList.append(part)

        return partList

    def get_movable_parts_bytype(self) -> dict[str, list[Part]]:
        partDict: dict[str, list[Part]] = {}
        movableList = self.get_movable_parts()
        for part in movableList:
            if part.type not in partDict:
                partDict[part.type] = []
            partDict[part.type].append(part)

        return partDict

    def __iter__(self):
        return self

    def __next__(self):
        if self.__curIndex < len(super().parts):
            member = super().parts[self.__curIndex]
            self.__curIndex += 1
            return member

        raise StopIteration

    


            



    
                

def main():
    robo = Robot('MTX', 'M1X', 'F-16', 10000)
    robo.add_part(Part(111, 100))
    robo.add_part(Part(222, 200))
    robo.add_part(Part(333, 300))
    robo.add_part(Part(222, 300))
    robo.add_part(MovablePart(555, 300, "TypeA"))
    robo.add_part(Part(111, 100))
    robo.add_part(Part(111, 100))
    robo.add_part(MovablePart(777, 300, "TypeB"))
    robo.add_part(MovablePart(655, 300, "TypeA"))
    robo.add_part(MovablePart(755, 300, "TypeA"))
    robo.add_part(MovablePart(977, 300, "TypeB"))
    robo.display()
    print()
    print("\nRobot test flight----")
    robo.fly()
    print("\nRobot dowork() test ----")
    robo.dowork()
    print("\nDuplicated part list----")
    partfreq = robo.find_duplicated_parts()
    for partno in partfreq.keys():
        print(partno,'=>', partfreq[partno], 'times')
    print("\nExpensive part list----")
    expensive_parts = robo.get_expensive_parts(200)
    for part in expensive_parts:
        part.display()
    print("\nMovable part list----")
    movable_parts = robo.get_movable_parts_bytype()
    for type, parts in movable_parts.items():
        print("type =", type)
        for part in parts:
            part.display()
    print()
    print("\nAsk movable to move----")
    movable_parts = robo.get_movable_parts()
    for part in movable_parts:
        part.move()
    print("\nTest remove_part() ----")
    robo.remove_part(333)
    for part in robo:
        if part.partno == 333:
            print('Found 333')
            break

if __name__ == "__main__":
    main()

