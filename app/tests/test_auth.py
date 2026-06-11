import pytest
from httpx import AsyncClient
from app.main import app
from app.core.database import Base, engine, AsyncSessionLocal
from app.usuarios.models.usuario import Usuario
from passlib.context import CryptContext
from sqlalchemy.future import select

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@pytest.fixture
async def client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

@pytest.fixture
async def db_session():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    async with AsyncSessionLocal() as session:
        yield session
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

@pytest.fixture
async def test_user(db_session):
    hashed_password = pwd_context.hash("password123")
    user = Usuario(
        us_nombre_usuario="testuser",
        us_correo="test@example.com",
        us_contrasena=hashed_password,
        us_cedula="1234567890"
    )
    db_session.add(user)
    await db_session.commit()
    await db_session.refresh(user)
    return user

@pytest.mark.asyncio
async def test_login_exitoso_con_correo(client, test_user):
    """Test de login exitoso usando correo electrónico."""
    response = await client.post("/usuarios/login", json={
        "identifier": "test@example.com",
        "password": "password123"
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

@pytest.mark.asyncio
async def test_login_exitoso_con_cedula(client, test_user):
    """Test de login exitoso usando cédula."""
    response = await client.post("/usuarios/login", json={
        "identifier": "1234567890",
        "password": "password123"
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

@pytest.mark.asyncio
async def test_login_fallido_usuario_no_existe(client):
    """Test de login fallido por usuario no encontrado."""
    response = await client.post("/usuarios/login", json={
        "identifier": "nonexistent@example.com",
        "password": "password123"
    })
    assert response.status_code == 404
    data = response.json()
    assert "detail" in data
    assert "no existe" in data["detail"]

@pytest.mark.asyncio
async def test_login_fallido_contrasena_incorrecta(client, test_user):
    """Test de login fallido por contraseña incorrecta."""
    response = await client.post("/usuarios/login", json={
        "identifier": "test@example.com",
        "password": "wrongpassword"
    })
    assert response.status_code == 401
    data = response.json()
    assert "detail" in data
    assert "inválidas" in data["detail"]