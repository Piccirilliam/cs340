#Example Python Code to Insert a Document
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps
import json
import urllib.parse

class AnimalShelter(object):
    #""" CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        print("Initializing AnimalShelter class...")  # Debug statement
        USER = urllib.parse.quote_plus(username)
        PASS = urllib.parse.quote_plus(password)
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30675
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient(f'mongodb://{USER}:{PASS}@{HOST}:{PORT}')
        self.database = self.client[DB]
        self.collection = self.database[COL]
        print("Connection Successful - Connected to:", HOST)

# Create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data) # Data should be a dictionary
            print("animal added succesfully")
            return True
        else:
            raise Exception("Nothing to save due to parameter being empty")
            

# Create method to implement the R in CRUD.
    def read(self, search=None):
        if search is not None:
            data = self.database.animals.find_one(search,{"_id": False})
            #for document in data:
                #print(document)
            
        else:
            data = self.database.animals.find_one({},{"_id": False})
        
        return data
    def read_all(self, search=None):
        if search is not None:
            data = self.database.animals.find(search,{"_id": False})
            #for document in data:
                #print(document)#debug code to ensure it was reading
            
        else:
            data = self.database.animals.find({},{"_id": False})
            
            
        
        return data

    
# Create method to implement the U in CRUD.
    def update(self, initial, change):
        if initial is not None:
            if self.database.animals.count_documents(initial, limit = 1) != 0:
                update_result = self.database.animals.update_many(initial, {"$set": change})
                result = update_result.raw_result
            else:
                result = "No document was found"
            return result
        else:
            raise Exception("Nothing to update, because data parameter is empty")

# Create method to implement the D in CRUD.
    def delete(self, remove):
        if remove is not None:
            if self.database.animals.count_documents(remove, limit = 1) != 0:
                delete_result = self.database.animals.delete_many(remove)
                result = delete_result.raw_result
            else:
                result = "No document was found"
            return result
        else:
            raise Exception("Nothing to delete, because data parameter is empty")