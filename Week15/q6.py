import enum
import csv


class EngineerProject:
    def __init__(self, engrName: str, salary: float, department: str) -> None:
        self.__engrName = engrName
        self.__salary = salary
        self.__department = department

    def __str__(self) -> str:
        return {f"The engrName is {self.__engrName}, the salary is {self.__salary}, the deparmtnet is {self.__department}"}
    

class ProjectType(enum.Enum):
    SOFTWARE = 0
    HARDWARE = 1
    MECHANICAL = 2

class Project:
    def __init__(self, projName: str, budget: float, projType: ProjectType) -> None:
        self.__projName = projName
        self.__budget = budget
        self.__projType = projType
        self.__milestones = [bool]

    @property
    def projType(self):
        return self.__projType

    @property
    def milestones(self):
        return self.__milestones

    @milestones.setter
    def milestones(self, milestones):
        self.__milestones = milestones

    def __str__(self) -> str:
        return {f"The projName is {self.__projName}, the budget is {self.__budget}, the projType is {self.__projType}, the milestones are {self.milestones}"}
    

class Engineer:
    def __init__(self, engrName: str, salary:float, department: str) -> None:
        self.__engrName = engrName
        self.__salary = salary
        self.__department = department
        self.__projects = [Project]

    @property
    def salary(self):
        return self.__salary
    
    @property
    def department(self):
        return self.__department

    @property
    def engrName(self):
        return self.__engrName

    @property
    def projects(self):
        return self.__projects
    
    @projects.setter
    def projects(self, projects):
        self.__projects = projects

    def csv_list(self) -> list:
        csvList = []
        csvList.append(self.engrName)
        csvList.append(self.salary)
        csvList.append(self.department)
        return csvList

    def __str__(self) -> str:
        return {f"The engrName is {self.__engrName}, the salary is {self.__salary}, the department is {self.__department}, the projects are {self.projects}"}


def getEngineerProjectList(engineerList : list[Engineer]) -> dict[str, EngineerProject]:
    dictionary1 = {}
    for engineer in engineerList:
        engineerProject = EngineerProject(engineer.engrName, engineer.salary, engineer.department)
        key = engineer.engrName
        dictionary1[key] = engineerProject
    return dictionary1

def getFastEngineers(engineerList : list[Engineer]) -> list[Engineer]:
    engineers = []
    for engineer in engineerList:
        for project in engineer.projects:
            if project.milestones[0] == True or project.milestones[1] == True or project.milestones[2] == True:
                engineers.append(engineer)
    
    return engineers


def getProjects(engineerList : list[Engineer]) -> dict[ProjectType, list[Project]]:
    dictionary = {}
    for engineer in engineerList:
        for project in engineer.projects:
            if dictionary.get(project.projType) == None:
                dictionary[project.projType] = [project]
            else:
                dictionary[project.projType].add(project)
    
    return dictionary


def saveFile( engineerList : list[Engineer], fileName : str ) -> None:
    with open(fileName, "w",  newline="") as file:
        writer = csv.writer(file)
        for engineer in engineerList:
            writer.writerow(engineer.csv_list())

def main():
    
    project1 = Project("Central", 500000, 1)
    project1.milestones = [True, True, False]
    project2 = Project("Control Office", 20000, 1)
    project2.milestones = [True, False, False]
    project3 = Project("Shooting Game", 10000, 0)
    project3.milestones = [True, True, True]
    project4 = Project("Company website", 7000, 0)
    project4.milestones = [True, False, False]
    project5 = Project("Shooting Game", 70000, 0)
    project5.milestones = [True, True, False]
    project6 = Project("Word Processor", 2000, 0)
    project6.milestones = [True, True,True]
    project7 = Project("Robot", 15000, 2)
    project7.milestones = [True, False, False]

    engineer1 = Engineer("Peter", 100000, "Electrical")
    engineer1.projects = [project1, project2]
    engineer2 = Engineer("Jim", 120000, "Software")
    engineer2.projects = [project3, project4, project5]
    engineer3 = Engineer("Nancy", 110000, "Software")
    engineer3.projects = [project6, project7]

    engineers = [engineer1, engineer2, engineer3]
    getEngineerProjectList(engineers)

    getFastEngineers(engineers)

    saveFile(engineers, "Engineers.csv")

if __name__ == "__main__":
    main()


    