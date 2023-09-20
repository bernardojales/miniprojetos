from pymongo import MongoClient

# tutorial link: https://pymongo.readthedocs.io/en/stable/tutorial.html
# examples: https://pymongo.readthedocs.io/en/stable/examples/index.html

host = 'localhost' # we will use localhost as host beacause we are connecting to mongodb server that is running using our host port
port = 27017 # the default port of mongodb service is 27017
username = "admin" # default username is admin
password = "admin" # default password is admin
database = "petshop" # database name

# you can pass connection parameters as kwargs
# client = MongoClient(host=host, port=port, username=username, password=password) # establish connection with mongodb server
# or you can pass connection parameters as URI
client = MongoClient(f"mongodb://{username}:{password}@{host}:{port}/") # establish connection with mongodb server

print(list(client.list_databases())) # list databases of mongodb server giving the name, size of each one
print(client.list_database_names()) # list databases names of mongodb server

db = client[database] # prepare to create database, but only creates when receive a create command to store data

# prepare to create collections, but only creates when receive a create command to store data
pet_collection = db["pets"]
store_collection = db["store"]

# collection.find() returns all documents in the collection
print("stores: ", list(store_collection.find()))

# observe that no database or collection was created
print(client.list_database_names())

# now we will send command to collection to store new documents
store = {"name":"petville"}
# docs of insertedResult type: https://pymongo.readthedocs.io/en/stable/api/pymongo/results.html#pymongo.results.InsertOneResult
insertResult = store_collection.insert_one(store)

# now we can check if the document has been created successfully
# first way is check the return of insert_one method
print("inserted: ", insertResult.acknowledged)
# second way is check if the document is present on the collection passing filters as parameters
print("stores: ", list(store_collection.find({"name":"petville"})))

# when some document is created, its add an id to the original variable that holds the information
# now store variable has the _id field added as result of insert_one operation
print(store["_id"])


# observe that database and collection was created
print(client.list_database_names())
print(db.list_collection_names())


# there are some validations that can be added to collection
# unique field validation
store_collection.create_index("name", unique=True)
# 

# try to insert a document with the same field value of already existing document
# raises DuplicateKeyError
from pymongo.errors import DuplicateKeyError
try:
    print("trying to save duplicated data")
    print(store_collection.insert_one({"name":"petville"}))
except DuplicateKeyError:
    print("DuplicateKeyError was raised")

# collection methods
# store_collection.find_one(filter) # search and returns one document or None if no document
# store_collection.find(filter) # search and returns all document or [] if no document
# store_collection.find(filter).limit(10) # search and returns the first 10 documents or [] if no document
# store_collection.update_one(filter, update_config) # search and update the first document that match with the passed filter
# store_collection.update_many(filter, update_config) # search and update all the documents that match with the passed filter
# store_collection.delete_one(filter) # delete the first document that match with the passed filter
# store_collection.delete_many(filter) # delete all documents that match with the passed filter

#------------------------------------------------------------------------------------------------------------------------------------------------

# challenge

# create some petshot store document and do CRUD operations with this document

#------------------------------------------------------------------------------------------------------------------------------------------------

# First way to do (hardcoded in classes)
class Store:
    def __init__(self, name, location, rating):
        self.name = name
        self.location = location
        self.rating = rating

class Pet:
    def __init__(self, name, species, age, store_id):
        self.name = name
        self.species = species
        self.age = age
        self.store_id = store_id

#------------------------------------------------------------------------------------------------------------------------------------------------

# Second way of doing it, with json documents: Create a petshop store document

store_doc = {
    "name": "Petland",
    "location": "Rua X",
    "rating": 4.5
}

# Insert the store document into the store_collection

store_collection.insert_one(store_doc)

# Check if the document has been inserted successfully

print("Petshop store document created:", store_doc)

#------------------------------------------------------------------------------------------------------------------------------------------------

# Challenge 2: create three pets that has a field as foreign_key with reference to the petshot store

#------------------------------------------------------------------------------------------------------------------------------------------------

#First way of doing:

# Create a Store object
petland = Store("Petland", "71 Rua X", 4.5)

# Insert the store document into the store_collection
store_collection.insert_one(petland.__dict__)

# Check if the document has been inserted successfully
print("Petshop store document created:", petland.__dict__)

# Create a Store object
petland = Store("Petland", "71 Rua X", 4.5)

# Insert the store document into the store_collection
store_collection.insert_one(petland.__dict__)

# Check if the document has been inserted successfully
print("Petshop store document created:", petland.__dict__)

# Create Pet objects and insert pet documents into the pet_collection
pets = [
    Pet("Ted", "Dog", 3, petland.__dict__["_id"]),
    Pet("Whiskers", "Cat", 2, petland.__dict__["_id"]),
    Pet("Rex", "Dog", 5, petland.__dict__["_id"])
]

pet_docs = [pet.__dict__ for pet in pets]

pet_collection.insert_many(pet_docs)

# Check if the pet documents have been inserted successfully
print("Three pet documents created:", pet_docs)

#------------------------------------------------------------------------------------------------------------------------------------------------

# Second way of doing it:

# Creating three pet documents with a foreign key reference to the store
pets = [
    {
        "name": "Ted",
        "species": "Dog",
        "age": 3,
        "store_id": store_doc["_id"]  # Use the _id of the store document as a reference
    },
    {
        "name": "Mel",
        "species": "Cat",
        "age": 2,
        "store_id": store_doc["_id"]
    },
    {
        "name": "Rex",
        "species": "Dog",
        "age": 5,
        "store_id": store_doc["_id"]
    }
]


# Insert the pet documents into the pet_collection
pet_collection.insert_many(pets)

# Check if the pet documents have been inserted successfully
print("Three pet documents created:", pets)

#------------------------------------------------------------------------------------------------------------------------------------------------

#Challenge 3: find all pets by petshop foreing_key filter

#------------------------------------------------------------------------------------------------------------------------------------------------

# First way of doing it: hardcoded

# Define the filter to find pets by store_id (foreign key)
store_id = petland.__dict__["_id"]
store_filter = {"store_id": store_id}

# Find all pets that belong to the "Pet Paradise" store
matching_pets = list(petland.find(store_filter))

# Print the matching pets
print("Pets in Petland:")
for pet in matching_pets:
    print(f"Name: {pet['name']}, Species: {pet['species']}, Age: {pet['age']}")

#------------------------------------------------------------------------------------------------------------------------------------------------

# Create a Store object
pet_paradise = Store("Petland", "71 Rua X", 4.5)

# Insert the store document into the store_collection
store_collection.insert_one(petland.__dict__)

# Check if the document has been inserted successfully
print("Petshop store document created:", petland.__dict__)


# Define the filter to find pets by store_id (foreign key)
store_filter = {"store_id": store_doc["_id"]}

# Find all pets that belong to the "Pet Paradise" store
matching_pets = list(pet_collection.find(store_filter))

# Print the matching pets
print("Pets in Petland:")
for pet in matching_pets:
    print(f"Name: {pet['name']}, Species: {pet['species']}, Age: {pet['age']}")

#------------------------------------------------------------------------------------------------------------------------------------------------

# drop collection
store_collection.drop()
# drop database
client.drop_database(database)
