from fastapi import APIRouter
from app.usuarios.api.v1.endpoints.registro import router as registro_router

# Crear el router principal para usuarios v1
router = APIRouter(prefix="/v1")

# Incluir los endpoints de registro
router.include_router(registro_router)