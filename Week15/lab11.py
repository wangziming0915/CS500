class Book:
    def __init__(self, isbn, title, author, price):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.price = price

class BookList:
    def __init__(self):
        self.__books = []

    @property
    def books(self):
        return self.__books

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def get_all_books(self):
        return self.books

    def find_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book

class OrderItem:
    def __init__(self, isbn, quantity):
        self.isbn = isbn
        self.quantity = quantity

class Orders:
    def __init__(self):
        self.order_items = []

    def add_order_item(self, order_item):
        self.order_items.append(order_item)

    def remove_order_item(self, order_item):
        self.order_items.remove(order_item)

    def get_all_order_items(self):
        return self.order_items

class Invoice:
    def __init__(self, total):
        self.total = total

from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class DisplayBookListCommand(Command):
    def __init__(self, book_list: BookList):
        self.book_list = book_list

    def execute(self):
        books = self.book_list.get_all_books()
        for book in books:
            print(f"The isbn is {book.isbn}, the title is {book.title}, the author is {book.author},the price is (${book.price})")

class SubmitOrderCommand(Command):
    def __init__(self, book_list, orders):
        self.book_list = book_list
        self.orders = orders

    def execute(self):
        while True:
            isbn = input("Enter the ISBN of the book you want to order: ")
            if isbn == 'done':
                break
            book = self.book_list.find_book_by_isbn(isbn)
            if book == None:
                print("Book not found.")
                continue
            quantity = int(input("Enter the quantity you want to order: "))
            order_item = OrderItem(isbn, quantity)
            self.orders.add_order_item(order_item)
        print("Order submitted.")

class DisplayInvoiceCommand(Command):
    def __init__(self, book_list, orders):
        self.book_list = book_list
        self.orders = orders

    def execute(self):
        total = 0
        order_items = self.orders.get_all_order_items()
        return order_items

def main():
    book_list = BookList()
    book1 = Book("11111", "Book 1", "Jack", 25.0)
    book2 = Book("22222", "Book 2", "Anna", 30.5)
    book_list.add_book(book1)
    book_list.add_book(book2)

    orders = Orders()

    while True:
        print("1. Display Book List")
        print("2. Submit Order")
        print("3. Display Invoice")
        print("4. Exit")
        choice = input("Please enter your option: ")

        if choice == '1':
            DisplayBookListCommand(book_list).execute()
        elif choice == '2':
            SubmitOrderCommand(book_list, orders).execute()
        elif choice == '3':
            DisplayInvoiceCommand(book_list, orders).execute()
        elif choice == '4':
            break
        else:
            print("Invalid input, please enter again")

if __name__ == "__main__":
    main()