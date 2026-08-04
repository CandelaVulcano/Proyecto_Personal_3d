from sqlalchemy.orm import Session

from src.models.pedido_item import PedidoItem
from src.config.database import SessionLocal

class PedidoItemRepository:
    def __init__(self, session: Session | None = None):
        self.session = session or SessionLocal()

    def create(self, pedido_id: int, producto_id: int, cantidad: int, precio_unitario: float) -> PedidoItem:
        pedido_item = PedidoItem(
            pedido_id=pedido_id,
            producto_id=producto_id,
            cantidad=cantidad,
            precio_unitario=precio_unitario,
        )
        self.session.add(pedido_item)
        self.session.commit()
        self.session.refresh(pedido_item)
        return pedido_item

    def get_by_id(self, pedido_item_id: int) -> PedidoItem | None:
        return self.session.query(PedidoItem).filter(PedidoItem.id == pedido_item_id).first()

    def get_all(self) -> list[PedidoItem]:
        return self.session.query(PedidoItem).all()

    def update(self, pedido_item: PedidoItem) -> PedidoItem:
        self.session.add(pedido_item)
        self.session.commit()
        self.session.refresh(pedido_item)
        return pedido_item

    def delete(self, pedido_item: PedidoItem) -> None:
        self.session.delete(pedido_item)
        self.session.commit()

    def close(self) -> None:
        self.session.close()