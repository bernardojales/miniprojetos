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

from sanic import Sanic, response
from sanic.exceptions import SanicException
from pydantic import ValidationError
import Pylance
import PyMongo
from repository import PetshopRepository, PetRepository
from models import PetshopModel, UpdatePetshopModel, PetModel, UpdatePetModel, ListPetshop, ListPet

app = Sanic(__name__)


#challenge 2, parte 3

@app.route('/petshop/<petshop_id>', methods=['GET'])
async def get_petshop(request, store_id):
    # Find the petshop by id
    petshop = await petshop_collection.find_one({'_id': ObjectId(store_id)})
    if petshop:
        # Format the response using PetshopModel
        petshop_model = PetshopModel(**petshop)
        return json(petshop_model.dict())
    else:
        return json({'error': 'Petshop not found'}, status=404)
    
#challenge 2, topico 4

from typing import List
from sanic import Sanic
from sanic.response import json
from pymongo import MongoClient
from bson import ObjectId
from pydantic import BaseModel

app = Sanic(__name__)

# Define o modelo Petshop
class Petshop(BaseModel):
    name: str
    location: str
    phone: int
    rating: float

# Define o modelo ListPetshop
class ListPetshop(BaseModel):
    __root__: List[Petshop]

# Conecte-se ao servidor MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['petshop']
petshop_collection = db['petshops']

# Defina o método GET para recuperar todos os petshops
@app.route('/petshops')
async def get_petshops(request):
    # Encontre todos os petshops na coleção
    petshops = await petshop_collection.find().to_list(length=None)
    # Formate a resposta usando ListPetshop
    response_data = ListPetshop(__root__=[Petshop(**petshop) for petshop in petshops])
    # Retorne a resposta como JSON
    return json(response_data.dict())

#parte 4

# Create instances of repositories
petshop_repository = PetshopRepository()
pet_repository = PetRepository()

# Endpoints for petshop collection
@app.route('/petshop', methods=['POST'])
async def create_petshop(request):
    # Validate input using PetshopModel
    data = request.json
    petshop_model = PetshopModel(**data)
    petshop_model.validate()

    # Insert data into petshop collection
    result = petshop_repository.create(data)
    
    # Format response using PetshopModel
    petshop_model.id = str(result.inserted_id)
    return response.json(petshop_model.dict(), status=201) #status code 201 means 'created' in HTTP

#parte 6

# Define o filtro para atualizar a loja de animais com o nome "Petland"

filter = {'name': 'Petland'}
# Define os dados atualizados para a loja de animais
updated_data = {'name': 'Petland', 'location': 'Rua Y', 'phone': '83991227888', 'rating': '4.8'}

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
    
""" # Part 2
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

"""
###creating the class for a template for managing connection with MongoDB

class MongoDBConnectionManager:
    def __init__(self, host, port, username, password):
        self.client = MongoClient(f"mongodb://{username}:{password}@{host}:{port}/")

    def get_database(self, database_name):
        return self.client[database_name]

    def close_connection(self):
        self.client.close()

"""
"""
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