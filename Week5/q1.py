class Person():
    def __init__(self, name: str) -> None:
        self.__name = name
    
    def dowork(self):
        print(f"Person {self.__name} is doing nothing.")

    def display(self):
        print(self)

    def __str__(self) -> str:
        return f"name = {self.__name}"

    @property
    def name(self) -> str:
        return self.__name

class Programmer(Person):
    def __init__(self, name: str, skills: str, salary: float) -> None:
        super().__init__(name)
        self.__skills = skills
        self.__salary = salary

    @property
    def skills(self) -> str:
        return self.__skills

    @property
    def salary(self) -> float:
        return self.__salary

    @property
    def name(self) -> str:
        return super().name

    def dowork(self) -> None:
        print(f"Programmer {super().name} is writing a program.")

    def get_annual_income(self) -> float:
        return self.__salary * 12

    def __str__(self) -> str:
        return f"{super().__str__()}\nskills = {self.__skills}\nsalary = {self.__salary}"

class Manager(Programmer):
    def __init__(self, name: str, skills: str, salary: float, bonus: float) -> None:
        super().__init__(name, skills, salary)
        self.__bonus = bonus

    @property
    def bonus(self) -> float:
        return self.__bonus

    def get_annual_income(self) -> float:
        return super().get_annual_income() + self.__bonus

    def dowork(self) -> None:
        print(f"Manager {self.name} is supervising a team of programmers.")

    def __str__(self) -> str:
        return f"{super().__str__()}\nbonus = {self.__bonus}"

class Project():
    def __init__(self, projname: str, budget: float, active: bool) -> None:
        self.__projname = projname
        self.__budget = budget
        self.__active = active

    @property
    def projname(self) -> str:
        return self.__projname

    @property
    def budget(self) -> float:
        self.__budget = 0.0
        return self.__budget

    @property
    def active(self) -> bool:
        self.__active = False
        return self.__active

    def display(self) -> None:
        print(f"projname = {self.__projname}")
        print(f"budget = {self.__budget}")
        print(f"active = {self.__active}")
    
class Group():
    def __init__(self, groupname: str) -> None:
        self.__members = []
        self.__groupname = groupname

    @property
    def members(self) -> list[Programmer]:
        return self.__members
    
    @property
    def groupname(self) -> str:
        return self.__groupname

    def add_member(self, programmer: Programmer) -> None:
        self.__members.append(programmer)

    def remove_member(self, name: str) -> None:
        for member in self.__members:
            if member.name == name:
                self.__members.remove(member)

    def ask_anyone_dowork(self) -> None:
        for member in self.__members:
            member.dowork()

    def ask_manager_dowork(self) -> None:
        for member in self.__members:
            if isinstance(member, Manager):
                member.dowork()

    def get_allmembers_morethan(self, income: float) -> list[Programmer]:
        members_morethan: list[Programmer] = []
        
        for member in self.__members:
            if member.get_annual_income() > income:
                members_morethan.append(member)

        return members_morethan

    def display(self) -> None:
        print(self)

    def __str__(self) -> str:
        output = f"Groupname: {self.__groupname}\n"
        output += f"The group has these members: \n"
        for member in self.__members:
            output += str(member) + "\n\n"
        return output
   


class ITGroup(Group):
    def __init__(self, groupname: str) -> None:
        super().__init__(groupname)
        self.__projects = []

    @property
    def projects(self) -> list[Project]:
        return self.__projects
        
    @property
    def groupname(self) -> str:
        return super().groupname

    @property
    def members(self) -> list[Programmer]:
        return super().members

    def add_project(self, project) -> None:
        self.__projects.append(project)

    def find_largest_project(self) -> Project:
        largest_project = self.__projects[0]

        for project in self.__projects:
            if project.budget > largest_project.budget:
                largest_project = project

        return project

    def get_active_projects(self) -> list[Project]:
        active_project_list = []

        for project in self.__projects:
            if project.active == True:
                active_project_list.append(project)

        return active_project_list

    def display(self) -> None:
        print("The group has these members:")
        for member in self.members:
            member.display()
            print()
        print("The group has these projects:")
        for project in self.__projects:
            project.display()
            print()

     

def main() -> None:
    p1: Programmer = Programmer("Lily", "C++, Java", 10000)
    p2: Programmer = Programmer("Judy", "Python, Java", 18000)
    m: Manager = Manager("Peter", "Management", 20000, 20000)
    proj1: Project = Project("MAX-5", 200000, True)
    proj2: Project = Project("FOX-4", 100000, False)
    proj3: Project = Project("FOX-XP", 500000, True)
    itgrp: ITGroup = ITGroup("ATX Group")
    itgrp.add_member(p1)
    itgrp.add_member(p2)
    itgrp.add_member(m)
    itgrp.add_project(proj1)
    itgrp.add_project(proj2)
    itgrp.add_project(proj3)
    itgrp.display()
    p3: Programmer = Programmer("Jone", "Python, Java", 1118000)
    itgrp.add_member(p3)
    itgrp.ask_anyone_dowork()
    print()
    itgrp.ask_manager_dowork()
    print("\nGet the largest project...")
    maxProj: list[Project] = itgrp.find_largest_project()
    if maxProj is not None:
        maxProj.display()
    print("\nGet the acive projects...")
    projects: list[Project] = itgrp.get_active_projects()
    for proj in projects:
        proj.display()
    print()
    itgrp.display()
    itgrp.remove_member(p3.name)
    print("\nGet the members with high income...")
    members: list[Programmer] = itgrp.get_allmembers_morethan(200000)
    for member in members:
        member.display()
    print()

if __name__ == "__main__":
    main()