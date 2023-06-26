from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

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
        USER = 'aacuser'
        PASS = 'Password123'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30791
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        print("Connection Successful")

    # Complete this Create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False

    # Create method to implement the R in CRUD.
    def read(self, search):
        if search is not None:
            if search:
                result = self.database.animals.find(search)
                for r in result:
                    return r
            else:
                exception = "Nothing to search because search param is empty"
                return exception

    # Create method to implement the U in CRUD.

    def update(self, query, data):
        if data is not None:
            data_update = self.database.animals.update_one(query, data)
            return data_update
        else:
            raise Exception("Nothing to update because data parameter is empty")

            # Create method to implement the D in CRUD.

    def delete(self, data):
        if data is not None:
            data_delete = self.database.animals.delete_one(data)
            return data_delete
        else:
            raise Exception("Nothing to delete because data parameter is empty")
            
