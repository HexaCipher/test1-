class LMS:
    def __init__(self,bookname, author, price, quantity):
        self.booknamae = bookname
        self.author = author
        self.price = price
        self.quantity = quantity

    def get_bookname(self):
        return self.booknamae
    def get_author(self):
        return self.author
    def get_price(self):
        return self.price
    def get_quantity(self):
        return self.quantity
    def set_bookname(self, bookname):
        self.booknamae = bookname
    def set_author(self, author):
        self.author = author    
    def set_price(self, price):
        self.price = price
    def set_quantity(self, quantity):
        self.quantity = quantity

    def display_book_info(self):
        print(f"Book Name: {self.booknamae}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")
        print(f"Quantity: {self.quantity}")



book1 = LMS("Python Programming", "John Doe", 500, 10)
book1.display_book_info()
book2 = LMS("Data Structures", "Jane Smith", 600, 5)
book2.display_book_info()
book3 = LMS("Machine Learning", "Alice Johnson", 800, 2)
book3.display_book_info()
book4 = LMS("Web Development", "Bob Brown", 700, 8)
book4.display_book_info()
    


        