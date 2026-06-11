from app.usuarios.repositories.usuario import get_usuario_by_email_or_cedula, create_usuario
from app.usuarios.schemas.usuario import UsuarioCreate
from sqlalchemy.ext.asyncio import AsyncSession
import re

# Expresión regular para validación de contraseña (ejemplo básico)
# Al menos 8 caracteres, una mayúscula, una minúscula y un número
PASSWORD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d@$!%*?&]{8,}$')

async def registrar_usuario(db: AsyncSession, usuario: UsuarioCreate):
    """
    Registra un nuevo usuario validando:
    - Unicidad de correo y cédula
    - Fortaleza de contraseña
    """
    # Verificar si ya existe un usuario con el mismo correo o cédula
    existing_user = await get_usuario_by_email_or_cedula(
        db, 
        correo=usuario.us_correo, 
        cedula=usuario.us_cedula
    )
    
    if existing_user:
        # Determinar qué campo está duplicado
        if existing_user.us_correo == usuario.us_correo:
            raise ValueError("El correo electrónico ya se encuentra registrado.")
        if existing_user.us_cedula == usuario.us_cedula:
            raise ValueError("La cédula ya se encuentra registrada.")
    
    # Validar contraseña
    if not PASSWORD_REGEX.match(usuario.us_contrasena):
        raise ValueError("La contraseña no cumple con los requisitos de seguridad.")
    
    # Crear el usuario
    usuario_dict = usuario.dict()
    return await create_usuario(db, usuario_dict)