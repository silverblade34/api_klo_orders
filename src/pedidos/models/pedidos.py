from pydantic import BaseModel

class PedidoItem(BaseModel):
    orderCreator: str
    name: str
    desRoute: str
    codeRoute: str
    roadmap: str
    direction: str
    latitude: float
    longitude: float
    codDestination: str
    nameDestination: str
    unit: str
    metersCubic: int
    weight: int
    desde: int
    hasta: int
    numBulto: str
    nGuia: str
    clienteName: str
    clienteruc: str
    business: str
