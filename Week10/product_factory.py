class Product:
    pass

class Computer(Product):
    pass

class Laptop(Product):
    pass

class Tablet(Product):
    pass


class ProductFactory:
    def create_product(self, type: str) -> Product:
        p: Product = None
        if type == "Computer":
            p = Computer()
        elif type == "Laptop":
            p = Laptop()
        elif type == "Tablet":
            p = Tablet()
        return p
    

def main():
    type = input("Enter the type of product:")
    factory1 = ProductFactory()
    p = factory1.create_product(type)