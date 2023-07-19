from ...mongo.connect import ConnectionMongo

class MongodPedidos:
    def __init__(self):
        self.connect = ConnectionMongo()

    def findOrders(self, business):
        db = self.connect.con
        col = db["orders"]
        col = col.find({"business": business}, {'_id': False})
        return col