from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
class Categoria(Base):
    __tablename__ = "categorias"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    descripcion: Mapped[str] = mapped_column(String(255), nullable=False)

    def __repr__(self) -> str:
        return (
            f"Categoria(id={self.id!r}, nombre={self.nombre!r}, "
            f"descripcion={self.descripcion!r})"
        )