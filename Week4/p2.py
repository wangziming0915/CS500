class Room:
    def __init__(self, type: str, size: int) -> None:
        self.__type = type
        self.__size = size

    @property
    def type(self) -> str:
        return self.__type
    
    @property
    def size(self) -> int:
        return self.__size
    
    def __str__(self) -> str:
        return f"Room type = {self.__type}, room size = {self.__size}"

class Garage:
    def __init__(self, type: str, size: int, door_type: str) -> None:
        self.__type = type
        self.__size = size
        self.__door_type = door_type
    
    @property
    def type(self) -> str:
        return self.__type

    @property
    def size(self) -> int:
        return self.__size

    @property
    def door_type(self) -> str:
        return self.__door_type

    def __str__(self) -> str:
        return f"Garage type = {self.__type}, size = {self.__size}, door_type = {self.__door_type}"

class Television:
    def __init__(self, screen_type: str, screen_size: int, resolution: str, price: float) -> None:
        self.__screen_type = screen_type
        self.__screen_size = screen_size
        self.__resolution = resolution
        self.__price = price

    @property
    def screen_type(self) -> str:
        return self.__screen_type

    @property
    def screen_size(self) -> int:
        return self.__screen_size

    @property
    def resolution(self) -> str:
        return self.__resolution

    @property
    def price(self) -> float:
        return self.__price

    def __str__(self) -> str:
        return f"Screen type = {self.__screen_type}, size = {self.__screen_size}, resolution = {self.__resolution}, price = {self.__price}"

class House:
    def __init__(self, address: str, square_feet: int, rooms: list[Room], garage: Garage, televisions: list[Television]) -> None:
        self.address = address
        self.square_feet = square_feet
        self.rooms = rooms
        self.garage = garage
        self.televisions = televisions
        
    def __str__(self) -> str:
        return f"House address = {self.address}, square_feet = {self.square_feet}, rooms = {self.rooms}, garage = {self.garage}, televisions = {self.televisions}"

    def remove_TV(self, television: Television) -> None:
        self.televisions.remove(television)
    
    def change_garage_size(self, wanted_size: int) -> None:
        self.garage.__size = wanted_size

    def get_biggest_room(self) -> Room:
        biggestRoom = self.rooms[0]
        for room in self.rooms:
            if room.size > biggestRoom.size:
                biggestRoom = room
        return biggestRoom

    def get_oled_televisions(self) -> list[Television]:
        list_of_TV = []
        for television in self.televisions:
            if television.screen_type == 'OLED':
                list_of_TV.append(television)
        return list_of_TV

    def is_similar_house(self, house2: "House") -> bool:
        if self.square_feet == house2.square_feet:
            return True
        return False

def main():
    garage1 = Garage("single", 50, "auto")
    room1 = Room("Bedroom", 20)
    room2 = Room("Bathroom", 50)
    television1 = Television("OLED", 65, "4K", 1500)
    television2 = Television("OLED", 65, "4K", 1300)
    house1 = House("165 str, 22 Apt", 120, [room1, room2], garage1, [television1, television2])
    house1.remove_TV(television1)
    print(house1.get_biggest_room().type)
    print(house1.get_oled_televisions()[0])

if __name__ == "__main__":
    main()


