# 30] Demonstrate step by step MongoDB connection in Python
import pymongo

# Step 1: Establish a connection to MongoDB
def Conn():
    try:
        # Connect to MongoDB server (default host and port)
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        print("Connected to MongoDB successfully!")
        return client
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB:", e)

# Step 2: Connect to a specific database
def Conn_to_database(client, database_name):
    try:
        # Access the specified database
        db = client[database_name]
        print(f"Connected to database '{database_name}' successfully!")
        return db
    except Exception as e:
        print("Error connecting to database:", e)

# Step 3: Access a specific collection within the database
def access_collection(db, collection_name):
    try:
        # Access the specified collection within the database
        collection = db[collection_name]
        print(f"Accessed collection '{collection_name}' successfully!")
        return collection
    except Exception as e:
        print("Error accessing collection:", e)

# Step 4: Perform CRUD operations or other tasks with the collection
def main():
    # Step 1: Connect to MongoDB
    client = Conn()

    # Step 2: Connect to a specific database
    database_name = "my_database"
    db = Conn_to_database(client, database_name)

    # Step 3: Access a specific collection within the database
    collection_name = "my_collection"
    collection = access_collection(db, collection_name)

    # Step 4: Perform CRUD operations or other tasks with the collection
    # For example, you can insert documents into the collection, query documents, update documents, delete documents, etc.

    # Close the MongoDB connection when done
    client.close()
    print("Connection to MongoDB closed.")

if __name__ == "__main__":
    main()
