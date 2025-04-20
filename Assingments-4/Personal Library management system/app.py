# Personal Library management system Streamlit Python Project -4

# Personal Library Management System

library = []

def show_menu():
    print("\n--- Personal Library Menu ---")
    print("1. Add a book")
    print("2. See book list") 
    print("3. Delete a book") 
    print("4. Exit")

def add_book():
    book = input("Enter book name: ")
    library.append(book)
    print(f"'{book}' has been added to your library.")

def view_books():
    if not library:
        print("Your library is empty.")
    else:
        print("\nHere is your book list:")   # updated message
        for i, book in enumerate(library, start=1):
            print(f"{i}. {book}")

def remove_book():
    book = input("Enter the name of the book to delete: ")  # updated prompt
    if book in library:
        library.remove(book)
        print(f"'{book}' has been deleted.")  # updated message
    else:
        print(f"'{book}' was not found in your library.")

# Main program loop
while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        remove_book()
    elif choice == "4":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
