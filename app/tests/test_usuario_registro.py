import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncSession
from app.main import app
from app.core.database import get_db
from app.usuarios.models.usuario import Usuario

client = TestClient(app)

# Fixture para la sesi贸n de base de datos (mock)
@pytest.fixture
def db_session_mock():
    # En un entorno real, usar铆as una base de datos de prueba
    # Aqu铆 simplemente simulamos la sesi贸n
    pass

# Prueba: Registro exitoso sin c茅dula
def test_registro_exitoso_sin_cedula():
    payload = {
        "us_correo": "test@example.com",
        "us_nombre": "Test",
        "us_apellido": "User",
        "us_contrasena": "ValidPass123!"
    }
    
    response = client.post("/api/usuarios/registrar", json=payload)
    
    # Verificar c贸digo de respuesta
    assert response.status_code == 201
    
    # Verificar estructura de la respuesta
    data = response.json()
    assert "message" in data
    assert "usuario" in data
    assert data["usuario"]["us_correo"] == payload["us_correo"]
    assert data["usuario"]["us_cedula"] is None

# Prueba: Registro exitoso con c茅dula
def test_registro_exitoso_con_cedula():
    payload = {
        "us_cedula": "1234567890",
        "us_correo": "test2@example.com",
        "us_nombre": "Test2",
        "us_apellido": "User2",
        "us_contrasena": "ValidPass123!"
    }
    
    response = client.post("/api/usuarios/registrar", json=payload)
    
    # Verificar c贸digo de respuesta
    assert response.status_code == 201
    
    # Verificar estructura de la respuesta
    data = response.json()
    assert "message" in data
    assert "usuario" in data
    assert data["usuario"]["us_correo"] == payload["us_correo"]
    assert data["usuario"]["us_cedula"] == payload["us_cedula"]

# Prueba: Registro fallido por correo duplicado
def test_registro_fallido_correo_duplicado():
    # Primero registramos un usuario
    payload1 = {
        "us_correo": "duplicate@example.com",
        "us_nombre": "Test1",
        "us_apellido": "User1",
        "us_contrasena": "ValidPass123!"
    }
    
    response1 = client.post("/api/usuarios/registrar", json=payload1)
    
    # Verificar que el primer registro fue exitoso
    assert response1.status_code == 201 or response1.status_code == 400 # Puede fallar si ya existe en DB
    
    # Ahora intentamos registrar otro usuario con el mismo correo
    payload2 = {
        "us_correo": "duplicate@example.com",
        "us_nombre": "Test2",
        "us_apellido": "User2",
        "us_contrasena": "ValidPass123!"
    }
    
    response2 = client.post("/api/usuarios/registrar", json=payload2)
    
    # Verificar c贸digo de error
    assert response2.status_code == 400
    
    # Verificar mensaje de error
    data = response2.json()
    assert "correo" in data["detail"].lower()

# Prueba: Registro fallido por c茅dula duplicada
def test_registro_fallido_cedula_duplicada():
    # Primero registramos un usuario
    payload1 = {
        "us_cedula": "9876543210",
        "us_correo": "test3@example.com",
        "us_nombre": "Test3",
        "us_apellido": "User3",
        "us_contrasena": "ValidPass123!"
    }
    
    response1 = client.post("/api/usuarios/registrar", json=payload1)
    
    # Verificar que el primer registro fue exitoso
    assert response1.status_code == 201 or response1.status_code == 400 # Puede fallar si ya existe en DB
    
    # Ahora intentamos registrar otro usuario con la misma c茅dula
    payload2 = {
        "us_cedula": "9876543210",
        "us_correo": "test4@example.com",
        "us_nombre": "Test4",
        "us_apellido": "User4",
        "us_contrasena": "ValidPass123!"
    }
    
    response2 = client.post("/api/usuarios/registrar", json=payload2)
    
    # Verificar c贸digo de error
    assert response2.status_code == 400
    
    # Verificar mensaje de error
    data = response2.json()
    assert "c茅dula" in data["detail"].lower()

# Prueba: Registro fallido por contrase帽a inv谩lida
def test_registro_fallido_contrasena_invalida():
    payload = {
        "us_correo": "test5@example.com",
        "us_nombre": "Test5",
        "us_apellido": "User5",
        "us_contrasena": "weak"  # No cumple con los requisitos de seguridad
    }
    
    response = client.post("/api/usuarios/registrar", json=payload)
    
    # Verificar c贸digo de error
    assert response.status_code == 422
    
    # Verificar mensaje de error
    data = response.json()
    assert "requisitos" in data["detail"].lower() or "seguridad" in data["detail"].lower()