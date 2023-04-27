class Professor:
    def __init__(self, prof_name: str) -> None:
        self.__name = prof_name

class Building:
    def __init__(self, building_name) -> None:
        self.__building_name = building_name
        self.__professors

    @property
    def building_name(self) -> str:
        return self.__building_name

    def add_professor(self, professor: Professor):
        self.__pro

class Department:
    def __init__(self) -> None:
        self.__professors: list[Professor] = []
        self.__buildings: list[Building] = []

    def add_professor(self, professor: Professor):
        self.__professors.append(professor)

    def add_building(self, building: Building):
        self.__buildings.append(Building(building.building_name))