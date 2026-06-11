from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class UsuarioCreate(BaseModel):
    us_cedula: Optional[str] = Field(None, max_length=20)
    us_correo: EmailStr = Field(..., max_length=100)
    us_nombre: str = Field(..., max_length=50)
    us_apellido: str = Field(..., max_length=50)
    us_contrasena: str = Field(..., min_length=8)

class UsuarioInDB(UsuarioCreate):
    us_codigo: str
    us_fecha_registro: datetime
    us_fecha_actualizacion: datetime

    class Config:
        from_attributes = True