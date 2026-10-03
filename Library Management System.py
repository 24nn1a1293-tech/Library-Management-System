library = []
def add_book():
    book_name = input("Enter Book Name:")
    library.append(book_name)
    print("Book Added Successfully!")
def view_books():
    if len(library) == 0:
        print("No Books Available")
    else:
        print("\nAvailable Books:")
        for book in library:
            print(book)
def search_book():
    book_name = input("Enter Book Name to Search:")
    if book_name in library:
        print("Book Found")
    else:
        print("Book Not Found")
def issue_book():
    book_name = input("Enter Book Name to Issue:")
    if book_name in library:
        library.remove(book_name)
        print("Book Issued Successfully!")
    else:
        print("Book Not Available")
def return_book():
    book_name = input("Enter Book Name to Return:")
    library.append(book_name)
    print("Book Returned Successfully")
def delete_book():
    book_name = input("Enter Book Name to Delete:")
    if book_name in library:
        library.remove(book_name)
        print("Book Deleted Successfully!")
    else:
        print("Book Not Found")
def main_menu():
    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Delete Book")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            issue_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            delete_book()
        elif choice == "7":
            print("Thank You!")
            break
        else:
            print("Invalid choice")
main_menu()