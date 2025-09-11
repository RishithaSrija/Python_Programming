# You are building a Library Management System in Python. The system should store books in a dictionary where:

# Key → Book ID
# Value → Book Title
# Write a Python program to perform the following operations using Dictionaries:

# Add a book to the library (Book ID, Title).
# Remove a book using Book ID.
# Search for a book by Book ID and display the title.
# Update the title of a book (e.g., correction in title).
# Display all books in the library.
# Count the total number of books in the library.
# Check if a book title exists in the library (reverse lookup).

def add_book(k, v, lib):
    lib[k] = v
    print(f"{k}, {v} added to library")

def remove_book(k, lib):
    if k in lib:
        del lib[k]
        print(f"Book ID {k} removed.")
    else:
        print("Book ID not found.")

def search_book(k, lib):
    if k in lib:
        print(f"{k} : {lib[k]} is found")
    else:
        print(f"Book ID {k} not found")

def update_book(k, new_title, lib):
    if k in lib:
        lib[k] = new_title
        print(f"Book ID {k} updated to '{new_title}'")
    else:
        print("Book ID not found.")

def display_books(lib):
    if lib:
        for k, v in lib.items():
            print(f"{k} : {v}")
    else:
        print("Library is empty.")

def count_books(lib):
    print(f"Total books: {len(lib)}")

def reverse_lookup(title, lib):
    found = [k for k, v in lib.items() if v == title]
    if found:
        print(f"Title '{title}' found with Book ID(s): {found}")
    else:
        print(f"Title '{title}' not found.")

def lib_manag():
    library = {}
    while True:
        print("\nLibrary Menu:")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Update book title")
        print("5. Display all books")
        print("6. Count total books")
        print("7. Reverse lookup by title")
        print("8. Exit")

        try:
            ch = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        match ch:
            case 1:
                key = int(input("Enter book ID: "))
                value = input("Enter book title: ")
                add_book(key, value, library)
            case 2:
                key = int(input("Enter book ID to remove: "))
                remove_book(key, library)
            case 3:
                key = int(input("Enter book ID to search: "))
                search_book(key, library)
            case 4:
                key = int(input("Enter book ID to update: "))
                new_title = input("Enter new title: ")
                update_book(key, new_title, library)
            case 5:
                display_books(library)
            case 6:
                count_books(library)
            case 7:
                title = input("Enter title to search: ")
                reverse_lookup(title, library)
            case 8:
                print("Exiting Library Manager.")
                break
            case _:
                print("Invalid choice. Try again.")

lib_manag()
