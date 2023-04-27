from abc import ABC, abstractmethod

class Calculator:
    @abstractmethod
    def calculate(self) -> str:
        pass

class SimpleCalculator(Calculator):
    def __init__(self) -> None:
        self.__nums: list[int] = []

    def add_num(self, num: int):
        self.__nums.append(num)

    def calculate(self) -> str:
        return f"The sum is {sum(self.__nums)}"
    
    def __iter__(self):
        self.__index = -1 # initialize index for each iteration
        return self
    
    def __next__(self) -> int:
        if self.__index >= len(self.__nums)-1:
            raise StopIteration()
        self.__index += 1
        num = self.__nums[self.__index]
        return num

class Decorator(Calculator):
    def __init__(self, calculator: Calculator) -> None:
        self.calculator = calculator

    def calculate(self) -> str:
        sum = self.calculator.calculate()

        average = sum(self.calculator) / len(self.calculator.__nums)

        return f"The sum is {sum}, and the average is {average}"

    def square_list(self) -> list:
        square = self.calculator.num
        
        return square

    def new_function(self) -> str:
        return "New"

def main():
    cal = SimpleCalculator()
    cal.add_num(10)
    cal.add_num(20)
    cal.add_num(30)
    print(cal.calculate())
    decorated_cal = Decorator(cal)
    print(decorated_cal.calculate())
    print(decorated_cal.square_list())
    print(decorated_cal.new_function())