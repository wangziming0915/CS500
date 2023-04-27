class Customer:
    def __init__(self, name: str, address: str) -> None:
        self.__name = name
        self.__address = address

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def address(self) -> str:
        return self.__address

    def __str__(self) -> str:
        #return "Customer name = " + self.__name + ",address = " + self.__address
        return f"Customer name = {self.__name}, address = {self.__address}"

class Product:
    def __init__(self, productid: int, product_name: str, price: float) -> None:
        self.__productid = productid
        self.__product_name = product_name
        self.__price = price

    @property
    def productid(self) -> int:
        return self.__productid

    @property
    def price(self) -> float:
        return self.__price

    def __str__(self) -> str:
        return f"Product product id = {self.__productid}, product name = {self.__product_name}, price = {self.__price}"

class OrderItem:
    def __init__(self, product: Product, quantity: int) -> None:
        self.__product = product
        self.__quantity = quantity

    @property
    def product(self) -> Product:
        return self.__product

    @property
    def quantity(self) -> int:
        return self.__quantity
    
    @property
    def total(self) -> float:
        return self.__product * self.__quantity

    def __str__(self) -> str:
        return f"Order item: Product = {self.__product}, quantity = {self.__quantity}"

    @quantity.setter
    def quantity(self,quantity) -> None:
        if quantity < 0:
            raise ValueError("The quantity cannot be a negative number.")

class Order:
    def __init__(self, orderid: int, customer: Customer) -> None:
        self.__orderid = orderid
        self.__customer = customer
        self.__order__items: list[OrderItem] = []

    def add_item(self, product: Product, quantity: int) -> None:
        found = False
        for item in self.__order__items:
            if item.product.productid == product.productid:
                item.quantity += quantity
                found = True
                
        if found == False:
            self.__order__items.append(OrderItem(product, quantity))

    def remove_item(self, productid: int):
        found = False
        for item in self.__order__items:
            if item.product.productid == productid:
                item.quantity = 0
                found = True
                
        if found == False:
            print("Item doesn't exist.")

    def find_largest_item(self) -> OrderItem:
        largest_item = OrderItem(1111, "Desk", 109.99)
        for item in self.__order__items:
            if item.total > largest_item.total:
                largest_item = item.product

        return largest_item

    def get_discount_value(self, discount_rate: float) -> float:
        total = 0
        for item in self.__order__items:
            total += item.total
        return total * discount_rate


    def get_total(self) -> float:
        total = 0
        for item in self.__order__items:
            total += item.total
        return total


    def __str__(self) -> str:
        return f"Order orderid = {self.__orderid}, Customer = {self.__customer}, items = {self.__order__items}"

    

def main():
    c = Customer("Peter", "Mission Blvd, Fremont")
    p1 = Product(1111, "Desk", 109.99)
    p2 = Product(2222, "Chair", 99.99)
    p3 = Product(3333, "Computer", 1109.99)
    print(c)

    order = Order(123,c)
    order.add_item(p1, 10)
    order.add_item(p2, 20)
    order.add_item(p3, 30)
    print(order)

if __name__ == "__main__":
    main()

    

