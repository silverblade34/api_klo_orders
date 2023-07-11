from fastapi import FastAPI 
from src.pedidos.routes.router import router
app = FastAPI()
app.include_router(router)
