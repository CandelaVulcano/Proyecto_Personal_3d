from fastapi import APIRouter

router = APIRouter(prefix="/productos", tags=["productos"])

@router.get("/")
def listar_productos():
    return {"mensaje": "Lista de productos"}