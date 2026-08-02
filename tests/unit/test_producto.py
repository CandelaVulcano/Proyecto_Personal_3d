from src.repositories.producto_repository import ProductoRepository
from src.services.producto_service import ProductoService


def test_registrar_producto_con_sesion_de_test(db_session):
    repo = ProductoRepository(session=db_session)
    service = ProductoService(repository=repo)

    producto = service.registrar_producto(
        nombre="Producto 1",
        descripcion="Descripción del producto 1",
        precio=100.0,
        stock=10,
    )

    assert producto.nombre == "Producto 1"
    assert producto.descripcion == "Descripción del producto 1"
    assert producto.precio == 100.0
    assert producto.stock == 10

