from src.repositories.producto_repository import ProductoRepository

class ProductoService:
    def __init__(self, repository: ProductoRepository | None = None):
        self.repository = repository or ProductoRepository()

    def registrar_producto(self, nombre: str, descripcion: str, precio: float):
        if not nombre:
            raise ValueError("El nombre del producto es obligatorio")

        if not descripcion:
            raise ValueError("La descripción del producto es obligatoria")

        if precio < 0:
            raise ValueError("El precio del producto no puede ser negativo")

        return self.repository.create(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
        )

    def obtener_producto_por_id(self, producto_id: int):
        return self.repository.get_by_id(producto_id)

    def listar_productos(self):
        return self.repository.get_all()