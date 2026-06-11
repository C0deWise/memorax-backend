from pydantic import BaseModel, Field
from typing import Union

class LoginRequest(BaseModel):
    """Esquema para la solicitud de inicio de sesi贸n."""
    identifier: str = Field(..., example="usuario@example.com", description="Correo electr贸nico o c茅dula del usuario")
    password: str = Field(..., example="contrase帽a_secreta", description="Contrase帽a del usuario")

class LoginResponse(BaseModel):
    """Esquema para la respuesta de inicio de sesi贸n exitoso."""
    access_token: str = Field(..., example="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...", description="Token de acceso JWT")
    token_type: str = Field(default="bearer", description="Tipo de token")