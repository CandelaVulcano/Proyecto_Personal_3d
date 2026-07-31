from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from src.services.usuario_service import UsuarioService

router = APIRouter(prefix="/usuarios", tags=["usuarios"])

service = UsuarioService()

class UsuarioCreate(BaseModel):
    nombre: str
    apellido: str
    email: str
    password_hash: str

@router.post("/")
def crear_usuario(usuario: UsuarioCreate):
    try:
        return service.registrar_usuario(
            nombre=usuario.nombre,
            apellido=usuario.apellido,
            email=usuario.email,
            password_hash=usuario.password_hash,
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/")
def listar_usuarios():
    return service.listar_usuarios()