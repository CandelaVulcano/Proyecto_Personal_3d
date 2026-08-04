from sqlalchemy.orm import Session

from src.models.pedido import Pedido
from src.config.database import SessionLocal

class PedidoRepository:
    def __init__(self, session: Session | None = None):
        self.session = session or SessionLocal()

    def create(self, usuario_id: int, total: float) -> Pedido:
        pedido = Pedido(
            usuario_id=usuario_id,
            total=total,
            estado="pendiente",
        )
        self.session.add(pedido)
        self.session.commit()
        self.session.refresh(pedido)
        return pedido

    def get_by_id(self, pedido_id: int) -> Pedido | None:
        return self.session.query(Pedido).filter(Pedido.id == pedido_id).first()

    def get_all(self) -> list[Pedido]:
        return self.session.query(Pedido).all()

    def update(self, pedido: Pedido) -> Pedido:
        self.session.add(pedido)
        self.session.commit()
        self.session.refresh(pedido)
        return pedido

    def delete(self, pedido: Pedido) -> None:
        self.session.delete(pedido)
        self.session.commit()

    def close(self) -> None:
        self.session.close()