#challenges estão no server.py, deixei esse arquivo só pra teste
from pymongo import MongoClient

host = 'localhost' 
port = 27017 
username = "admin" 
password = "admin" 
database = "petshop" 

client = MongoClient(f"mongodb://{username}:{password}@{host}:{port}/") 

db = client[database]

pet_collection = db["pets"]
store_collection = db["store"]

print("stores: ", list(store_collection.find()))