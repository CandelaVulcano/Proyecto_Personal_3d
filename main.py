from fastapi import FastAPI
from src.api.routes.usuario import router as usuario_router
from src.api.routes.producto import router as producto_router
from src.api.routes.carrito import router as carrito_router

app = FastAPI()

app.include_router(usuario_router)
app.include_router(producto_router)
app.include_router(carrito_router)