# Proyecto_Personal_3d

## Descripción

Proyecto Python con FastAPI, SQLAlchemy y PostgreSQL. Usa Alembic para migraciones y `python-dotenv` para cargar la configuración de la base de datos.

## Modelo de las tablas de la base de datos

Usuario
   │
   ├──────────────┐
   ▼              ▼
Carrito         Pedido
   │              │
   ▼              ▼
CarritoItem   PedidoItem
      │             │
      └──────┬──────┘
             ▼
          Producto
             │
             ▼
         Categoría

Producto
   │
   ▼
Imagen

Pedido
   │
   ▼
Pago

Pedido
   │
   ▼
Dirección

## Requisitos previos

- Python 3.11+ o compatible
- PostgreSQL instalado localmente o acceso a una base de datos remota
- un entorno virtual para instalar dependencias

## Instalación

1. Activar el entorno virtual:

```powershell
.\.venv\Scripts\Activate.ps1
```

2. Instalar dependencias:

```powershell
python -m pip install -r requirements.txt
```

## Configurar la base de datos

### Opción 1: usar PostgreSQL local instalado

Crea un archivo `.env` en la raíz del proyecto con la URL de conexión a PostgreSQL:

```env
DATABASE_URL=postgresql+psycopg2://usuario:contraseña@localhost:5432/mi_db_local
```

### Opción 2: usar PostgreSQL con Docker

Si prefieres no instalar PostgreSQL localmente, puedes iniciar la base con Docker.

```powershell
docker compose up -d
```

Verifica que el contenedor esté activo:

```powershell
docker compose ps
```

Si necesitas detener la base de datos:

```powershell
docker compose down
```

Luego usa este `.env`:

```env
DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/proyecto_personal_3d
```

> No subas tu `.env` al repositorio. Agrega `.env` a `.gitignore` si aún no está.

## Migraciones

Para aplicar el esquema de base de datos:

```powershell
alembic upgrade head
```

Si se crean nuevos modelos, genera una migración así:

```powershell
alembic revision --autogenerate -m "mensaje descriptivo"
alembic upgrade head
```

## Ejecutar la aplicación

Usa Uvicorn para levantar el backend:

```powershell
uvicorn main:app --reload
```

La API quedará disponible en `http://127.0.0.1:8000`.

## Estructura importante

- `main.py`: punto de entrada de la aplicación FastAPI
- `src/api/routes/`: routers por dominio (usuarios, productos, carritos)
- `src/services/`: lógica de negocio
- `src/repositories/`: acceso a datos y consultas
- `src/models/`: modelos SQLAlchemy
- `alembic/`: migraciones de base de datos

## Compartir el proyecto con otros desarrolladores

Cada desarrollador debe:

1. clonar el repositorio
2. crear su propio `.env` local
3. instalar dependencias
4. ejecutar `alembic upgrade head`

Opcional: si se usa una base de datos de desarrollo compartida, todos pueden apuntar a la misma `DATABASE_URL`, pero lo más seguro es usar bases locales independientes.

## Notas

- `fastapi` es el framework web
- `uvicorn` es el servidor ASGI que ejecuta la app
- `SQLAlchemy` es el ORM
- `psycopg2-binary` es el driver de PostgreSQL
- `alembic` gestiona migraciones
- `python-dotenv` carga variables de entorno

## Tests

Para ejecutarlos ejecuta: .\.venv\Scripts\python.exe -m pytest -q
Para listar los unit test: dir tests\unit