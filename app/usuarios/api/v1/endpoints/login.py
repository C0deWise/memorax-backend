from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.usuarios.schemas.login import LoginRequest, LoginResponse
from app.usuarios.services.auth_service import AuthService

router = APIRouter(prefix="/usuarios", tags=["usuarios"])

@router.post("/login", response_model=LoginResponse)
async def login(login_data: LoginRequest, db: AsyncSession = Depends(get_db)):
    """
    Endpoint para autenticar a un usuario y generar un token de acceso.
    
    Args:
        login_data: Datos de inicio de sesión (identifier y password).
        db: Sesión de base de datos.
        
    Returns:
        LoginResponse: Token de acceso JWT.
    """
    # Autenticar usuario
    user = await AuthService.authenticate_user(login_data.identifier, login_data.password, db)
    
    # Crear token de acceso
    access_token = AuthService.create_access_token(
        data={"sub": str(user.us_codigo), "email": user.us_correo}
    )
    
    return LoginResponse(access_token=access_token)