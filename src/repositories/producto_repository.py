from sqlalchemy.orm import Session

from src.models.producto import Producto
from src.config.database import SessionLocal

class ProductoRepository:
    def __init__(self, session: Session | None = None):
        self.session = session or SessionLocal()

    def create(self, nombre: str, descripcion: str, precio: float) -> Producto:
        producto = Producto(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            stock=0,
            activo=True,
            categoria_id=1  # Asignar un valor predeterminado para categoria_id
        )
        self.session.add(producto)
        self.session.commit()
        self.session.refresh(producto)
        return producto

    def get_by_id(self, producto_id: int) -> Producto | None:
        return self.session.query(Producto).filter(Producto.id == producto_id).first()

    def get_all(self) -> list[Producto]:
        return self.session.query(Producto).all()

    def update(self, producto: Producto) -> Producto:
        self.session.add(producto)
        self.session.commit()
        self.session.refresh(producto)
        return producto

    def delete(self, producto: Producto) -> None:
        self.session.delete(producto)
        self.session.commit()

    def close(self) -> None:
        self.session.close()
