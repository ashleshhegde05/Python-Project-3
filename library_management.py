# Library Management System using OOP

class Library:

    def __init__(self):
        self.books = []

    def add_book(self):
        book = input("Enter Book Name: ")
        self.books.append(book)
        print("Book Added Successfully!")

    def remove_book(self):
        book = input("Enter Book Name to Remove: ")

        if book in self.books:
            self.books.remove(book)
            print("Book Removed Successfully!")
        else:
            print("Book Not Found.")

    def issue_book(self):
        book = input("Enter Book Name to Issue: ")

        if book in self.books:
            self.books.remove(book)
            print("Book Issued Successfully!")
        else:
            print("Book Not Available.")

    def return_book(self):
        book = input("Enter Book Name to Return: ")
        self.books.append(book)
        print("Book Returned Successfully!")

    def display_books(self):
        if len(self.books) == 0:
            print("No Books Available.")
        else:
            print("\nAvailable Books:")
            for book in self.books:
                print("-", book)


library = Library()

while True:

    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.remove_book()

    elif choice == "3":
        library.issue_book()

    elif choice == "4":
        library.return_book()

    elif choice == "5":
        library.display_books()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")