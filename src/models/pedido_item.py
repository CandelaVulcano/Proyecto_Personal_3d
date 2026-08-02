from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

class PedidoItem(Base):
    __tablename__ = "pedido_items"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    pedido_id: Mapped[int] = mapped_column(ForeignKey("pedidos.id"), nullable=False)
    producto_id: Mapped[int] = mapped_column(ForeignKey("productos.id"), nullable=False)
    cantidad: Mapped[int] = mapped_column(nullable=False)
    precio_unitario: Mapped[float] = mapped_column(nullable=False)

    def __repr__(self) -> str:
        return (
            f"PedidoItem(id={self.id!r}, pedido_id={self.pedido_id!r}, "
            f"producto_id={self.producto_id!r}, cantidad={self.cantidad!r}, precio_unitario={self.precio_unitario!r})"
        )
