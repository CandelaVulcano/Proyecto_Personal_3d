from sqlalchemy.orm import Session

from src.models.usuario import Usuario
from src.config.database import SessionLocal


class UsuarioRepository:
    def __init__(self, session: Session | None = None):
        self.session = session or SessionLocal()

    def create(self, nombre: str, apellido: str, email: str, password_hash: str, telefono: str) -> Usuario:
        usuario = Usuario(
            nombre=nombre,
            apellido=apellido,
            email=email,
            password_hash=password_hash,
            telefono=telefono,
        )
        self.session.add(usuario)
        self.session.commit()
        self.session.refresh(usuario)
        return usuario

    def get_by_id(self, usuario_id: int) -> Usuario | None:
        return self.session.query(Usuario).filter(Usuario.id == usuario_id).first()

    def get_by_email(self, email: str) -> Usuario | None:
        return self.session.query(Usuario).filter(Usuario.email == email).first()

    def get_all(self) -> list[Usuario]:
        return self.session.query(Usuario).all()

    def update(self, usuario: Usuario) -> Usuario:
        self.session.add(usuario)
        self.session.commit()
        self.session.refresh(usuario)
        return usuario

    def delete(self, usuario: Usuario) -> None:
        self.session.delete(usuario)
        self.session.commit()

    def close(self) -> None:
        self.session.close()
