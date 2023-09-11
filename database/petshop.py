from sanic import Sanic, response
from sanic.exceptions import NotFound
from pymongo import MongoClient
from bson import ObjectId
import asyncio
from pymongo import MongoClient

client = MongoClient()

class PetShop:
    def data (self, input):
        
