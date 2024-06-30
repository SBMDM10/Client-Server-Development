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
        USER = username
        PASS = password
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30079
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    """ Method that implements the C in CRUD. The Create method. Uses self, the information used to communicate with the database, and data, which is the argument information, to insert data into the database. Specfically checks that the id generated for a new entry is indeed in the database and returns True. If that id is not found,  or data argument is empty, returns False. """

    def create(self, data):
        if len(data) != 0:
            check_result = self.database.animals.insert_one(data)
            if check_result.inserted_id:
                return True
            else:
                return False
        else:
            return False

    """ Method that implements the R in CRUD. The Read method. Uses self and data to find database entries that possess matches for information queried from data. Method returns all keys and values for each entry a match is found with. Method returns an empty list if no matches are found. Method returns entire database if the data query is empty. """
    def read(self, data):
        if len(data) != 0:
            printable = list(self.database.animals.find(data, {'_id': False}))
            return printable
        else:
            printable = list(self.database.animals.find())
            return printable

    """ Method that implements the U in CRUD. The Update method. Uses self, data, and updateDate, the argument value that a match will update to, to search for and update any matches in the database. Returns the number of documents modified with the method call. If the input data, or updateData, is empty returns an error message. """
    def update(self, data, updateData):
        if len(data) != 0 and len(updateData) != 0:
            printable = self.database.animals.update_many(data, {'$set': updateData})
            return printable.modified_count
        else:
            return ('Queried argument was empty!')
    """ Method that implements the D in CRUD. The Delete method. Uses self and data to search for and delete any matches to the argument values in data. Returns the number of documents deleted with the method call. If the input data is empty it returns an error message. """
    def delete(self, data):
        if len(data) != 0:
            printable = self.database.animals.delete_many(data)
            return printable.deleted_count
        else:
            return ('Queried argument was empty!')