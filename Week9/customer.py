class Customer:
    def __init__(self, acc_number: int, first_name: str, last_name: str, balance: float) -> None:
        self.__acc_number = acc_number
        self.__first_name = first_name
        self.__last_name = last_name
        self.__balance = balance

    @property
    def acc_number(self) -> int:
        return self.__acc_number
    
    @property
    def first_name(self) -> str:
        return self.__first_name
    
    @property
    def last_name(self) -> str:
        return self.__last_name
    
    @property
    def balance(self) -> float:
        return self.__balance

    def __str__(self) -> str:
        return f"account number: {self.__acc_number}, first_name: {self.__first_name}, last_name: {self.__last_name}, balance: {self.__balance}"
    
    def get_csv(self) -> list[str]:
        csv_str: list[str] = [str(self.__acc_number), self.__first_name, self.__last_name, str(self.__balance)]
        return csv_str
    
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Customer):
            return __o.__acc_number == self.__acc_number
        else:
            return False