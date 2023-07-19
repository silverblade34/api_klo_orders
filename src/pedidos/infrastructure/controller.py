from src.pedidos.application.response import PedidosResponse
from src.pedidos.infrastructure.mongod import MongodPedidos

class PedidosController:
    def __init__(self):
        self.mongo = MongodPedidos()
        self.response = PedidosResponse()
        
    def listarPedidos(self):
        dataParsed = self.response.parsedOrders()
        listaOrders = self.mongo.findOrders()
        return listaOrders