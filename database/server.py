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

# challenge
# create some petshot store document and do CRUD operations with this document
# create three pets that has a field as foreign_key with reference to the petshot store
# find all pets by petshop foreing_key filter

# drop collection
store_collection.drop()
# drop database
client.drop_database(database)
