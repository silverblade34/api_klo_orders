from fastapi import APIRouter, HTTPException, status
from src.pedidos.models.pedidos import PedidoItem
from typing import List
router = APIRouter()

#MOSTRAR DATOS
@router.post("/api/v1/orders/insert")
async def setUserParsed(pedido_list: List[PedidoItem]):
    pedidos = pedido_list
    print(pedidos)
    return {"pedido": pedidos}