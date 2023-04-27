#1. Rack and Box - Aggregation;  note: A Rack object has a list of Box objects
class Box:
    def __init__(self) -> None:
        pass

class Rack:
    def __init__(self) -> None:
        self.boxes = []

    def add_box(self, box: Box):
        self.boxes.append(box)

#2. Computer and Memory - Composition;  note: A Computer object has one Memory Object
class Memory:
    def __init__(self) -> None:
        pass

class Computer:
    def __init__(self) -> None:
        self.memory = Memory()

#3. Train and Passenger - Aggregation;   note: A Train object has a list of Passenger object
class Passenger:
    def __init__(self) -> None:
        pass

class Train:
    def __init__(self) -> None:
        self.passengers = []

    def add_box(self, passenger: Passenger):
        self.passengers.append(passenger)

#4. Chair and Leg - Composition: note A Chair object has four legs of varying length.
class Leg:
    def __init__(self) -> None:
        pass

class Chair:
    def __init__(self) -> None:
        self.leg1 = Leg()
        self.leg2 = Leg()
        self.leg3 = Leg()
        self.leg4 = Leg()
        self.legs = []
