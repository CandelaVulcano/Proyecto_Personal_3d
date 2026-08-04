from src.repositories.usuario_repository import UsuarioRepository
from src.services.usuario_service import UsuarioService


def test_registrar_usuario_con_sesion_de_test(db_session):
    repo = UsuarioRepository(session=db_session)
    service = UsuarioService(repository=repo)

    usuario = service.registrar_usuario(
        nombre="Ana",
        apellido="Pérez",
        email="ana@test.com",
        password_hash="hash1234",
    )

    assert usuario.email == "ana@test.com"
    assert usuario.nombre == "Ana"
    assert usuario.apellido == "Pérez"
