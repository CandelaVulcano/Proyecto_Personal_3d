from datetime import datetime, timezone

from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

class Pago(Base):
    __tablename__ = "pagos"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    pedido_id: Mapped[int] = mapped_column(ForeignKey("pedidos.id"), nullable=False)
    medio_pago: Mapped[str] = mapped_column(nullable=False)
    estado: Mapped[str] = mapped_column(nullable=False)
    monto: Mapped[float] = mapped_column(nullable=False)
    fecha: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
    
    def __repr__(self) -> str:
        return (
            f"Pago(id={self.id!r}, pedido_id={self.pedido_id!r}, "
            f"medio_pago={self.medio_pago!r}, estado={self.estado!r}, monto={self.monto!r}, fecha={self.fecha!r})"
        )


