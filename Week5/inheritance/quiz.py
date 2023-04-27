class Professor():
    def __init__(self, professor_name: str, full_time: bool, salary: float) -> None:
        self.professor_name = professor_name
        self.full_time = full_time
        self.salary = salary

    def __str__(self) -> str:
        return (f"The professor name is {self.professor_name}, the full time is {self.full_time}, the salary is {self.salary}.")


class Building():
    def __init__(self, building_name: str, stories: int) -> None:
        self.building_name = building_name
        self.stories = stories
        self.professors = []

    def __str__(self) -> str:
        return (f"The building name is {self.building_name}, the stories is {self.stories}.")

    def add_professor(self, professor: Professor):
        self.professors.append(professor)

    def remove_parttime_professors(self):
        for professor in self.__professors:
            if professor.full_time == False:
                self.professors.remove(professor)

    def get_professor_with_highest_salary(self) -> Professor:
        result = self.__professors[0]
        for professor in self.professors:
            if professor.salary > result.salary:
                result = professor
        
        return result


class Department():
    def __init__(self, deptname: str) -> None:
        self.__deptname = deptname
        self.__professors = []
        self.__buildings = []

    @property
    def deptname(self) -> None:
        return self.__deptname

    @deptname.setter
    def deptname(self, deptname: str) -> None:
        self.__deptname = deptname

    def add_building(self, building: Building):
        self.__buildings.append(building)

    def add_professor(self, professor: Professor):
        self.__professors.append(professor)

    def remove_professor(self, professor_name: str):
        for professor in self.__professors:
            if professor.professor_name == professor_name:
                self.__professors.remove(professor)

    def get_fulltime_professors(self) -> list[Professor]:
        result = []
        for professor in self.__professors:
            if professor.full_time == True:
                result.append(professor)

        return result

    def get_buildings_by_stories(self, stories: int) -> list[Building]:
        result = []
        for building in self.__buildings:
            if building.stories == stories:
                result.append(building)

        return result


    def get_professors_by_buildings(self, building_name: str) -> list[Professor]:
        result = []
        for building in self.__buildings:
            if building.building_name == building_name:
                result = building.__professors
        
        return result

    def __str__(self) -> str:
        return (f"The depart name is {self.__deptname}.")


def main():
    professor1: Professor = Professor("Dylan", True, 20)
    professor2: Professor = Professor("Wong", False, 15)
    building1: Building = Building("Building1", 1)
    building2: Building = Building("Building2", 2)
    department: Department = Department("Home Department")
    print(professor1.__str__())
    print(professor2.__str__())
    building1.add_professor(professor1)
    building2.add_professor(professor2)
    print(building1.__str__())
    for professor in building1.professors:
        print(professor.__str__())
    department.add_building(building1)
    department.add_building(building2)


    

if __name__ == "__main__":
    main()

    