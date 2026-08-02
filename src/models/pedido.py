from datetime import datetime, timezone

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

class Pedido(Base):
    __tablename__ = "pedidos"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"), nullable=False)
    fecha: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
    estado: Mapped[str] = mapped_column(String(20), default="pendiente", nullable=False)
    total: Mapped[float] = mapped_column(nullable=False)
    direccion_id: Mapped[int] = mapped_column(ForeignKey("direcciones.id"), nullable=False)
