"""
# Challenge
## Part 1
1. Create a infrastructure layer responsible to manage mongodb connection and provide database access;
2. Use the provided database to create repository layer to create a petshop repository that uses 'petshop' colletion;
3. Create pet repository that uses 'pet' collection;
4. Create endpoints to create, update, find_all, find_one and delete_one documents of 'petshop' collection;
5. Create endpoints to create, update, find_all, find_one and delete_one documents of 'pet';

# Part 2
1. Create a PetshopModel to validate the user input and add as functionality on POST method;
2. Use the PetshopModel to format the return of POST method;
3. Use the PetshopModel to format the return of GET method on get_one;
4. Use the ListPetshop to format the return of GET method on get_all;
5. Use the UpdatePetshopModel to validate the user input and add as functionality on PATCH method;
6. Use the PetshopModel to format the return of PATCH method on update_one;
7. Use the PetModel to validate the user input and add as functionality on POST method;
8. Use the PetModel to format the return of POST method;
9. Use the PetModel to format the return of GET method on get_one;
10. Use the ListPet to format the return of GET method on get_all;
11. Use the UpdatePetModel to validate the user input and add as functionality on PATCH method;
12. Use the PetModel to format the return of PATCH method on update_one

# Part 3
1. Create an auto reconnection to database, test it with 'docker compose down' and 'docker compose up -d mongo' commands, do requests when database is down and repeat when database is up;
2. Identify database disconnection status and log it;

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



"""


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

"""