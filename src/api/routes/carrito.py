from fastapi import APIRouter

router = APIRouter(prefix="/carritos", tags=["carritos"])

@router.get("/")
def listar_carritos():
    return {"mensaje": "Lista de carritos"}