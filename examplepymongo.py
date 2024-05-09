import pymongo
from pymongo.server_api import ServerApi

# Connect to MongoDB Atlas
client = pymongo.MongoClient("mongodb+srv://aiswaryajoypp:u1358@cluster0.kddhga6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",server_api=ServerApi('1'))
db = client["LoginData"]

# Specify the collection name
collection = db["logindataa"]

# Insert a document into the collection
result = collection.insert_one({"user3": "user132"})

# Print the inserted document's ID
print("Inserted document ID:", result.inserted_id)
print(result.acknowledged)
print(result)
print(collection.database)
