from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.usuarios.schemas.usuario import UsuarioCreate
from app.usuarios.services.usuario import registrar_usuario
from app.core.database import get_db

router = APIRouter()

@router.post("/usuarios/registrar", status_code=status.HTTP_201_CREATED)
async def registrar_nuevo_usuario(
    usuario: UsuarioCreate,
    db: AsyncSession = Depends(get_db)
):
    """
    Endpoint para registrar un nuevo usuario.
    
    Valida:
    - Unicidad de correo y cédula
    - Fortaleza de contraseña
    
    Retorna:
    - 201 Created: Usuario registrado exitosamente
    - 400 Bad Request: Correo o cédula duplicados
    - 422 Unprocessable Entity: Contraseña no válida
    """
    try:
        nuevo_usuario = await registrar_usuario(db, usuario)
        return {
            "message": "Usuario registrado exitosamente",
            "usuario": {
                "us_codigo": nuevo_usuario.us_codigo,
                "us_correo": nuevo_usuario.us_correo,
                "us_nombre": nuevo_usuario.us_nombre,
                "us_apellido": nuevo_usuario.us_apellido,
                "us_cedula": nuevo_usuario.us_cedula,
                "us_fecha_registro": nuevo_usuario.us_fecha_registro
            }
        }
    except ValueError as e:
        # Determinar el código de estado adecuado
        if "requisitos de seguridad" in str(e):
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=str(e)
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e)
            )