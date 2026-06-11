from app.core.database import get_db
from app.usuarios.models.usuario import Usuario
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta
from app.core.config import settings
from fastapi import HTTPException, status

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthService:
    """Servicio para gestionar la autenticaci贸n de usuarios."""

    @staticmethod
    async def authenticate_user(identifier: str, password: str, db: AsyncSession) -> Usuario:
        """
        Autentica un usuario por correo o c茅dula y contrase帽a.

        Args:
            identifier: Correo electr贸nico o c茅dula del usuario.
            password: Contrase帽a proporcionada.
            db: Sesi贸n de base de datos.

        Returns:
            Usuario si las credenciales son v谩lidas.

        Raises:
            HTTPException: Si el usuario no existe o las credenciales son inv谩lidas.
        """
        # Buscar usuario por correo o c茅dula
        stmt = select(Usuario).where(
            (Usuario.us_correo == identifier) | (Usuario.us_cedula == identifier)
        )
        result = await db.execute(stmt)
        user = result.scalar_one_or_none()

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="El usuario no existe en el sistema"
            )

        # Verificar contrase帽a
        if not pwd_context.verify(password, user.us_contrasena):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciales inv谩lidas"
            )

        return user

    @staticmethod
    def create_access_token(data: dict) -> str:
        """
        Crea un token de acceso JWT.

        Args:
            data: Datos a incluir en el token.

        Returns:
            Token JWT firmado.
        """
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
        return encoded_jwt