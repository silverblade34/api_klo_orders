from multiprocessing import connection
from pymongo import MongoClient
from bson.binary import UuidRepresentation
class ConnectionMongo:

    def __init__(self):
        #_ NAME DB
        db = "dblogisticsv2"
        connection = MongoClient('mongodb://URI', uuidRepresentation='standard')
        self.con = connection[db]
