from abc import ABC, abstractmethod

class Displayable(ABC):

class House(Displayable):
    def __init__(self, address, squareFeet, numOfRooms, price: float) -> None:
        self.__address = address
        self.__squareFeet = squareFeet
        self.__numOfRooms = numOfRooms
        self.__price = price

    def __str__(self) -> str:
        return f"Address = {self.__address}, Square Feet = {self.__squareFeet}, Number of rooms = {self.__numOfRooms}, price = {self.__price}"
    
    def display(self):
        print(self)

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, House):
            return self.__address == __o.__address
        else:
            return False
        
class Contact(Displayable):
    def __init__(self, firstName, lastName, phoneNumber, email) -> None:
        self.__firstName = firstName
        self.__lastName = lastName
        self.__phoneNumber = phoneNumber
        self.__email = email
    
    def __str__(self) -> str:
        return f"Last"
    
    def display(self):
        print(self)

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Contact):
            return self.__email == __o.__email and self.__phoneNumber == __o.__phoneNumber
        else:
            return False
        
class Owner(Contact):
    def __init__(self, firstName, lastName, phoneNumber, email) -> None:
        super().__init__(firstName, lastName, phoneNumber, email)
        self.__houses = []

    def addHouse(self, house):
        self.__houses.append(house)

    def display(self):
        super().display()
        print("Owns the following houses:")
        for house in self.__houses:
            house.display()

class Buyer(Contact):
    def __init__(self, firstName, lastName, phoneNumber, email) -> None:
        super().__init__(firstName, lastName, phoneNumber, email)
        self.__watchList = []

    @property
    def watchList(self):
        return self.__watchList
    
    def saveForLater(self, house: House):
        if house not in self.watchList:
            self.__watchList.append(house)

    def removeFromSaveForLater(self, house: House):
        if house in self.watchList:
            self.watchList.remove(house)

    def display(self):
        super().display()
        print("Watching the following houses:")
        for house in self.watchList:
            house.display()

class Company(Displayable):
    def __init__(self, companyName) -> None:
        self.__companyName = companyName
        self.__owners = []
        self.__buyers = []
        self.__agents = []
        self.__houses = []

    def addOwner(self, owner):
        if owner not in self.__owners:
            self.__owners.append(owner)

    def addBuyer(self, buyer):
        pass

    def addAgent(self, agent):
        pass

    def addHouseToListing(self, house):
        if house not in self.__houses:
            self.__houses.append(house)

    def getHouseByAddress(self, address: str):
        house = House(address, 0,0,0)
        if house in self.__houses:
            idx = self.__houses.index(house)
            return self.__houses[idx]
        else:
            return None

    def removeHouseFromListing(self, house):
        pass

    def removeHouseFromSaveForLater(self, house):
        for buyer in self.__buyers:
            buyer.removeFromSaveForLater(house)
        
    def getBuyerByHouse(self, house):
        pass

    def display(self):
        pass

class Agent(Contact):
    def __init__(self, firstName, lastName, phoneNumber, email, position, company) -> None:
        super().__init__(firstName, lastName, phoneNumber, email)
        self.__position = position
        self.__company = company

    def addHouseToListingForOwner(self, owner, house):
        self.__company.addOwner(owner)
        self.__company.addHouseToListing(house)

    def helpBuyerToSaveForLater(self, buyer: Buyer, house):
        self.__company.addBuyer(buyer)
        buyer.saveForLater(house)

    def editHousePrice(self, address, newPrice):
        pass

    def soldHouse(self, house):
        self.__company.removeHouseFromListing(house)

        self.__company.removeHouseFromSaveForLater(house)


    def printPotentialBuyers(self, house):
        pass

    def display(self):
        super().display()
        pass