from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['Sample']

print("Connection established")

collection = db['Table1']

data = {
    "_id":None,
    "name":"Vaibhav Mahajan",
    "Gender":"male"
}

# Uncomment the following lines if you want to insert data
# for i in range(4,100):
#     data["_id"] = i
#     collection.insert_one(data)

# print("All the data has been inserted successfully")

# fetch = collection.find({"_id": {"$gt": 50}})
# for i in fetch:
#     print(i)

# Uncomment the following lines if you want to update a record
# update = collection.update_one({"_id":2},{"$set":data})
# print("Record has been updated successfully")

delete = collection.delete_one({"_id":6})

for f in range(4,100):
    fetch = collection.delete_one({"_id":f})
    print(fetch)





-----------------------------------------------------------------------------------------------
import pymongo.mongo_client as mc

conn = mc.MongoClient('localhost', 27017)

db = conn["Organisation"]

collection = db["EMP"]

data = [
    {'Name': 'Alice', 'Age': 25, 'Occupation': 'Engineer','salary': 50000},
    {'Name': 'Bob', 'Age': 30, 'Occupation': 'Manager','salary': 5000},
    {'Name': 'Charlie', 'Age': 35, 'Occupation': 'Data Scientist','salary': 10000},
    {'Name': 'David', 'Age': 40, 'Occupation': 'Software Developer','salary': 7000},
    {'Name': 'Eve', 'Age': 45, 'Occupation': 'Data Analyst','salary': 80000},
    {'Name': 'Frank', 'Age': 50, 'Occupation': 'Manager','salary': 9000},
    {'Name': 'Grace', 'Age': 55, 'Occupation': 'Data Scientist','salary': 100000},
    {'Name': 'Helen', 'Age': 60, 'Occupation': 'Software Developer','salary': 110000},
    {'Name': 'Ivy', 'Age': 65, 'Occupation': 'Data Analyst','salary': 120000},
    {'Name': 'John', 'Age': 70, 'Occupation': 'Engineer','salary': 130000}


]

result = collection.insert_many(data)

# Display the collection
# display = collection.find()
# for record in display:
#     print(record)

# Accessing specific columns
# print("Accessing specific columns:")
# find = collection.find({"salary": {"$gt": 5000 , "$lt": 10000}})
# for record in find:
#     print(record)


update = collection.update_one({"Name": "Alice"}, {"$set": {"Occupation": "Data"}})

for i in collection.find().sort('Age'):
    print(i)
    
    
    
-----------------------------------------------------------------------------------------------





# Write a python program using MongoDB database to create a “Books”
# collection having fields: title, Author (a list), Publisher, PubAddress, (a
# dict with keys like area, city, country), Price, ISBN. Accept input from
# user to insert documents

from pymongo import MongoClient

def insert_book(collection):
    """
    Function to insert a book document into the collection.
    """
    title = input("Enter title of the book: ")
    author = input("Enter author(s) of the book (comma-separated): ").split(',')
    publisher = input("Enter publisher of the book: ")
    pub_area = input("Enter publication area: ")
    pub_city = input("Enter publication city: ")
    pub_country = input("Enter publication country: ")
    price = float(input("Enter price of the book: "))
    isbn = input("Enter ISBN of the book: ")

    # Create dictionary for publication address
    pub_address = {
        "area": pub_area,
        "city": pub_city,
        "country": pub_country
    }

    # Create book document
    book = {
        "title": title,
        "author": author,
        "publisher": publisher,
        "pub_address": pub_address,
        "price": price,
        "ISBN": isbn
    }

    # Insert document into collection
    collection.insert_one(book)
    print("Book document inserted successfully!")

def main():
    # Connect to MongoDB
    client = MongoClient('localhost', 27017)
    db = client['library']
    collection = db['Books']

    # Accept input from user to insert documents
    while True:
        insert_book(collection)
        choice = input("Do you want to insert another book? (yes/no): ")
        if choice.lower() != 'yes':
            break

    # Close MongoDB connection
    client.close()

if __name__ == "__main__":
    main()
