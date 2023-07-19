from fastapi import APIRouter, HTTPException, status
from src.pedidos.models.pedidos import PedidoItem
from src.pedidos.infrastructure.controller import PedidosController
from typing import List
router = APIRouter()

#MOSTRAR DATOS
@router.post("/api/v1/orders/list")
async def listOrders(pedido_list: List[PedidoItem]):
    _pediCL = PedidosController()
    data = _pediCL.listarPedidos()
    return {"pedido": data}