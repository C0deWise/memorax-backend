from pydantic import BaseModel, Field
from typing import Union

class LoginRequest(BaseModel):
    """Esquema para la solicitud de inicio de sesión."""
    identifier: str = Field(..., example="usuario@example.com", description="Correo electrónico o cédula del usuario")
    password: str = Field(..., example="contraseña_secreta", description="Contraseña del usuario")

class LoginResponse(BaseModel):
    """Esquema para la respuesta de inicio de sesión exitoso."""
    access_token: str = Field(..., example="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...", description="Token de acceso JWT")
    token_type: str = Field(default="bearer", description="Tipo de token")