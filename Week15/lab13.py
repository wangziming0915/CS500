from abc import ABC

class Book:
    def __init__(self, isbn, title, author, price):
        self.__isbn = isbn
        self.title = title
        self.author = author
        self.price = price

    @property
    def isbn(self):
        return self.__isbn

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Book) and __o.__isbn == self.__isbn

    def __str__(self) -> str:
        return f"Book isbn={self.isbn}, title={self.title}, author={self.author}, price={self.price}"


class BookList:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def find_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def display_books(self):
        for book in self.books:
            print(book.__str())

class OrderItem:
    def __init__(self, isbn, quantity):
        self.__isbn = isbn
        self.__quantity = quantity

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, OrderItem) and __o.__isbn == self.__isbn
    
    def __str__(self) -> str:
        return f"OrderItem isbn={self.__isbn}, quantity={self.__quantity}"

class Order:
    def __init__(self):
        self.__items = []

    @property
    def items(self):
        return self.__items

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self, book_list: BookList):
        total = 0.0
        for item in self.items:
            book = book_list.find_book_by_isbn(item.isbn)
            if book:
                total += book.price * item.quantity
        return total

class Invoice:
    def __init__(self, order: Order, book_list: BookList) -> None:
        self.__order = order
        self.__book_list = book_list
    
    def getInvoice(self) -> int:
        sum = 0
        for order_item in self.__order.__order_items:
            for book in self.__book_list: 
                if book.__isbn ==  order_item.__isbn:
                    sum += book.price * order_item.__quantity
        
        return sum

class Command(ABC):
    def execute(self):
        pass

class DisplayBookListCommand(Command):
    def __init__(self, book_list):
        self.book_list = book_list

    def execute(self):
        self.book_list.display_books()


class SubmitOrderCommand(Command):
    def __init__(self, book_list: BookList, orders):
        self.book_list = book_list
        self.orders = orders

    def execute(self):
        while True:
            isbn = input("Enter the ISBN of the book you want to order: ")
            if isbn == 'done':
                break
            book = self.book_list.find_book_by_isbn(isbn)
            if book:
                quantity = int(input("Enter the quantity you want to order: "))
                item = OrderItem(isbn, quantity)
                self.orders.add_item(item)
                print(f"Book added.")
            else:
                print("Book not found.")


class DisplayInvoiceCommand(Command):
    def __init__(self, book_list, orders):
        self.book_list = book_list
        self.orders = orders

    def execute(self):
        invoice = Invoice(self.orders, self.book_list)
        items = invoice.__book_list
        for item in items:
            print(item)

class Invoker:
    def __init__(self) -> None:
        self.__commands = []

    def add_command(self, command):
        self.__commands.append(command)

    def execute_command(self, command_no) -> str:
        return self.__commands[command_no - 1].execute()


class BookApplication:
    def __init__(self) -> None:
        self.__order = Order()
        self.__invoker = Invoker()
        self.__booklist = BookList()

    @property
    def order(self):
        return self.__order

    @property
    def booklist(self):
        return self.__booklist

    def add_command(self, command):
        self.__invoker.add_command(command)

    def process_command(self, command_no):
        print(self.__invoker.execute_command(command_no))

def main():
    book_list = BookList()
    orders = Order()
    invoice = Invoice(orders, book_list)
    invoker = Invoker()

    book_list.add_book(Book("111", "ABC", "Jack", 10.5))
    book_list.add_book(Book("222", "DEF", "Janny", 22.0))
    book_list.add_book(Book("333", "FGT", "Anna", 12.5))
    book_list.add_book(Book("444", "AAS", "Dylan", 20.5))

    display_book_list_command = DisplayBookListCommand(book_list)
    submit_order_command = SubmitOrderCommand(orders, book_list)
    display_invoice_command = DisplayInvoiceCommand(orders, invoice)

    while True:
        print("Select an option:")
        print("1. Display book list")
        print("2. Submit order")
        print("3. Display invoice")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            invoker.add_command(display_book_list_command)
            invoker.execute_command()

        elif choice == "2":
            invoker.add_command(submit_order_command)
            invoker.execute_command()

        elif choice == "3":
            invoker.add_command(display_invoice_command)
            invoker.execute_command()

        elif choice == "4":
            break

        else:
            print("Invalid input, please enter again")

if __name__ == "__main__":
    main()