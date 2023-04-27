from customer import Customer
from db import CustomerRepository

class Bank:
    def __init__(self, bank_name) -> None:
        self.__bank_name = bank_name
        self.__customers: list[Customer] = []
    
    @property
    def customers(self) -> list[Customer]:
        return self.__customers
    
    @property
    def bank_name(self) -> str:
        return self.__bank_name

    def add_customer(self, customer: Customer):
        if customer in self.__customers:
            print(f"Customer already exists.")
        else:
            self.__customers.append(customer)


    def remove_customer(self, customer_number: int):
        for customer in self.__customers:
            if customer.__acc_number == customer_number:
                self.__customers.remove(customer)
        else:
            print(f"Could not find the customer.")

    def update_customer(self, customer: Customer) -> None:
        if customer in self.__customers:
            self.__customers.remove(customer)

        self.__customers.append(customer)