from abc import ABC, abstractmethod

class NewLibInterface(ABC):
    @abstractmethod
    def compute(self, nums_dict: dict[int, int]) -> float:
        pass

class NewLibConcrete(NewLibInterface):
    def compute(self, nums_dict: dict[int, int]) -> float:
        sum = 0
        count = 0

        for key in nums_dict:
            count += nums_dict[key]
            sum += key * nums_dict[key]

        return sum / count

class LibInterface(ABC):
    @abstractmethod
    def compute(self, freq_array: list[int]) -> float:
        pass

    @abstractmethod
    def compute_debug(self, freq_array: list[int], message: str) -> None:
        pass

#Adapter
class NewLibAdapter(LibInterface):
    def __init__(self, new_lib_con: NewLibConcrete):
        self.new_lib_con = new_lib_con

    def compute(self, freq_array: list[int]) -> float:
        nums_dict = {}
        for i in range(len(freq_array)):
            nums_dict.update(i = freq_array[i])

        return self.new_lib_con.compute(nums_dict)

    def compute_debug(self, freq_array: list[int], message: str):
        nums_dict = {}
        for i in range(len(freq_array)):
            nums_dict.update(i = freq_array[i])

        average = self.new_lib_con.compute(nums_dict) 
        print(f"{message} {average}")
#End of Adapter

class LibConcrete(LibInterface):
    def compute(self, freq_array: list[int]) -> float:
        sum = 0
        count = 0

        for i in range(len(freq_array)):
            count += freq_array[i]
            sum += i * freq_array[i]

        return sum / count

    def compute_debug(self, freq_array: list[int], message: str) -> None:
        average = self.compute(freq_array) 
        print(f"{message} {average}")

class Factory:
    def get_lib(self):
        return LibConcrete()

def main():
    lib = Factory().get_lib()
    average = lib.compute([2, 0, 5, 1, 8])
    print("The average =", average)
    lib.compute_debug([2, 0, 5, 1, 8], "The average =")


if __name__ == "__main__":
    main()