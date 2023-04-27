class Tire:
    def __init__(self, size) -> None:
        self.__size = size

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, size):
        self.__size = size

    def __str__(self) -> str:
        return f"Tire size: {self.__size}"# Instead of self.__size, self.size would be better since it's a property.
    
    def __repr__(self) -> str:
        return str(self)


class Car:
    def __init__(self, model, tires) -> None:
        self.__model = model
        if len(tires) != 4:
            raise ValueError("4 tires are required.")
        #It would be better if there is an "else". Since if the length of tires does not meet 4, the initialization of self.__tires should not be excuted.
        self.__tires = [tires[0], tires[1], tires[2], tires[3]]
        #Instead of directly referring to tires[n], it would be better if it initialize 4 Tire objects then append them into self.__tires. 

    @property
    def model(self):
        return self.__model
    
    @property
    def tires(self):
        return self.__tires

class main():
    try:
        c = Car("M7", [Tire(21), Tire(21), Tire(21), Tire(21)])
        print(c.model)
        print(c.tires)
        for tire in c.tires:
            tire.size = 22
        print(c.tires)
    except Exception as e:
        print(f"Do Nothing because {e}")

#Would be better if "if __name__ == "__main__":" was added here.

    main()