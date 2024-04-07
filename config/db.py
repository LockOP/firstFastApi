from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
# MongoDB Atlas connection string
# Replace "your_connection_string" with your actual connection string
MONGO_CONNECTION_STRING = os.getenv("MONGO_CONNECTION_STRING")


# Function to connect to MongoDB
def connect_to_mongodb():
    try:
        # Connect to MongoDB Atlas
        client = MongoClient(MONGO_CONNECTION_STRING)
        # Access a specific database (replace "your_database" with the actual database name)
        db = client.student
        # Return the database object
        print("Connected to MongoDB")
        print(MONGO_CONNECTION_STRING)
        return db
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        return None

# Example usage:
# db = connect_to_mongodb()
# if db:
#     print("Connected to MongoDB!")
#     # Perform database operations here
# else:
#     print("Failed to connect to MongoDB.")
