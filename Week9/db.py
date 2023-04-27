from customer import Customer
import csv

class CustomerRepository:
    def __init__(self, filename: str = "customer.csv") -> None:
        self.__filename = filename

    def read_customers(self) -> list[Customer]:
        customers: list[Customer] = []

        with open(self.__filename, newline = "") as file:
            reader = csv.reader(file)

            for row in reader:
                customer = Customer(int(row[0]), row[1], row[2], float(row[3]))
                customers.append(customer)

        return customers
    
    def write_customers(self, customers: list[Customer]):
        with open(self.__filename, "w") as file:
            writer = csv.writer(file)
            for customer in customers:
                writer.writerow(customer.get_csv())

def main():
    db = CustomerRepository()
    customers = db.read_customers()
    for customer in customers:
        print(customer)

    customer = Customer(444, "Jack", "Li", 300)
    customers.append(customer)

    db.write_customers(customers)

if __name__ == "__main__":
    main()