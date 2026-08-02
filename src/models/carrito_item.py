from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .carrito import Carrito

class CarritoItem(Base):
    __tablename__ = "carrito_items"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    carrito_id: Mapped[int] = mapped_column(ForeignKey("carritos.id"), nullable=False)
    producto_id: Mapped[int] = mapped_column(ForeignKey("productos.id"), nullable=False)
    cantidad: Mapped[int] = mapped_column(Integer, nullable=False, default=1)

    carrito: Mapped["Carrito"] = relationship(back_populates="items")
