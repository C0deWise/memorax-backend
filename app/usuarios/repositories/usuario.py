from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import or_
from app.usuarios.models.usuario import Usuario
from app.core.security import hash_password

async def get_usuario_by_email_or_cedula(db: AsyncSession, correo: str, cedula: str = None):
    """Obtiene un usuario por correo o cédula."""
    query = select(Usuario).where(
        or_(
            Usuario.us_correo == correo,
            Usuario.us_cedula == cedula
        )
    )
    result = await db.execute(query)
    return result.scalars().first()

async def create_usuario(db: AsyncSession, usuario_data: dict):
    """Crea un nuevo usuario con contraseña hasheada."""
    # Hashear la contraseña
    usuario_data['us_contrasena'] = hash_password(usuario_data['us_contrasena'])
    
    # Crear instancia del modelo
    db_usuario = Usuario(**usuario_data)
    
    # Guardar en base de datos
    db.add(db_usuario)
    await db.commit()
    await db.refresh(db_usuario)
    
    return db_usuario