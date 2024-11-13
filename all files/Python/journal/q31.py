# 32] Write a Menu Driver Program to add, display, search, sort and exit in book database
# containing
# Book_id, Book_name, Book_author through Python-MongoDB connectivity.
import pymongo

# Function to connect to MongoDB
def Conn():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["book_database"]
    collection = db["books"]
    return collection

# Function to add a book record
def add_book(collection):
    book_id = input("Enter Book ID: ")
    book_name = input("Enter Book Name: ")
    book_author = input("Enter Book Author: ")
    book = {"Book_id": book_id, "Book_name": book_name, "Book_author": book_author}
    collection.insert_one(book)
    print("Book added successfully!")

# Function to display all book records
def display_books(collection):
    books = collection.find()
    for book in books:
        print(book)

# Function to search for a book by name
def search_book(collection):
    book_name = input("Enter Book Name to search: ")
    books = collection.find({"Book_name": book_name})
    for book in books:
        print(book)

# Function to sort books by name
def sort_books(collection):
    books = collection.find().sort("Book_name")
    for book in books:
        print(book)

# Main function
def main():
    collection = Conn()
    while True:
        print("\nMenu:")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Search Book")
        print("4. Sort Books")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_book(collection)
        elif choice == "2":
            display_books(collection)
        elif choice == "3":
            search_book(collection)
        elif choice == "4":
            sort_books(collection)
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
