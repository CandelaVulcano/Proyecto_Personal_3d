from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

class Direccion(Base):
    __tablename__ = "direcciones"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"), nullable=False)
    calle: Mapped[str] = mapped_column(nullable=False)
    numero: Mapped[str] = mapped_column(nullable=False)
    ciudad: Mapped[str] = mapped_column(nullable=False)
    provincia: Mapped[str] = mapped_column(nullable=False)
    codigo_postal: Mapped[str] = mapped_column(nullable=False)

    def __repr__(self) -> str:
        return (
            f"Direccion(id={self.id!r}, usuario_id={self.usuario_id!r}, "
            f"calle={self.calle!r}, numero={self.numero!r}, ciudad={self.ciudad!r}, provincia={self.provincia!r}, codigo_postal={self.codigo_postal!r})"
        )
