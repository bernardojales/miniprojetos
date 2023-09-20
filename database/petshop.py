from sanic import Sanic, response
from sanic.exceptions import NotFound
from pymongo import MongoClient
from bson import ObjectId
import asyncio
import json
from pymongo import MongoClient

client = MongoClient()

class PetShop:
    def data (self, x):
        self.x = input("enter data")
#challenges estão no server.py, deixei esse arquivo só pra teste