from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

class Imagen(Base):
    __tablename__ = "imagenes_producto"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    producto_id: Mapped[int] = mapped_column(ForeignKey("productos.id"), nullable=False)
    url: Mapped[str] = mapped_column(nullable=False)
    orden: Mapped[int] = mapped_column(nullable=False)

    def __repr__(self) -> str:
        return (
            f"Imagen(id={self.id!r}, producto_id={self.producto_id!r}, "
            f"url={self.url!r}, orden={self.orden!r})"
        )
