#creating the class for a template for managing connection with MongoDB

class MongoDBConnectionManager:
    def __init__(self, host, port, username, password):
        self.client = MongoClient(f"mongodb://{username}:{password}@{host}:{port}/")

    def get_database(self, database_name):
        return self.client[database_name]

    def close_connection(self):
        self.client.close()

"""
creating petshop repository and pet repository
~~~repository is a design pattern used in software development to abstract and encapsulate the data access logic for a specific data source or collection
of data. In this case, the "repository" classes, namely PetshopRepository and PetRepository, are responsible for interacting with and managing data 
in MongoDB collections

These classes serve as a layer of abstraction that separates the business logic of an application from the details
of how data is retrieved, updated, or deleted in the underlying data store

"""

"""
what each repository do:


~~PetshopRepository:

Manages interactions with the "petshop" collection in the MongoDB database.
Provides methods to perform CRUD (Create, Read, Update, Delete) operations on documents within the "petshop" collection.
Encapsulates the data access logic, abstracting it away from the rest of the application.


~~ PetRepository:

Manages interactions with the "pet" collection in the MongoDB database.
Provides methods to perform CRUD operations on documents within the "pet" collection.
Like PetshopRepository, it abstracts the data access logic for the "pet" collection.

"""
class PetshopRepository:
    def __init__(self, database):
        self.collection = database["petshop"]

    def create(self, data):
        return self.collection.insert_one(data)

    def update(self, filter, update_data):
        return self.collection.update_one(filter, {"$set": update_data})

    def find_all(self):
        return list(self.collection.find())

    def find_one(self, filter):
        return self.collection.find_one(filter)

    def delete_one(self, filter):
        return self.collection.delete_one(filter)


class PetRepository:
    def __init__(self, database):
        self.collection = database["pet"]

    def create(self, data):
        return self.collection.insert_one(data)

    def update(self, filter, update_data):
        return self.collection.update_one(filter, {"$set": update_data})

    def find_all(self):
        return list(self.collection.find())

    def find_one(self, filter):
        return self.collection.find_one(filter)

    def delete_one(self, filter):
        return self.collection.delete_one(filter)

