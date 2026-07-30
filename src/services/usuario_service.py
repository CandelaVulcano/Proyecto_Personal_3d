from src.repositories.usuario_repository import UsuarioRepository


class UsuarioService:
    def __init__(self, repository: UsuarioRepository | None = None):
        self.repository = repository or UsuarioRepository()

    def registrar_usuario(self, nombre: str, apellido: str, email: str, password_hash: str):
        if not nombre or not apellido:
            raise ValueError("Nombre y apellido son obligatorios")

        if not email or "@" not in email:
            raise ValueError("Email inválido")

        if self.repository.get_by_email(email):
            raise ValueError("El email ya está registrado")

        return self.repository.create(
            nombre=nombre,
            apellido=apellido,
            email=email,
            password_hash=password_hash,
        )

    def obtener_usuario_por_id(self, usuario_id: int):
        return self.repository.get_by_id(usuario_id)

    def listar_usuarios(self):
        return self.repository.get_all()
