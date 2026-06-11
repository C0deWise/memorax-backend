from fastapi import FastAPI
from app.core.config import Settings
from app.core.database import engine, Base
from app.usuarios.api.v1.routes import router as usuarios_v1_router

# Instancia de la aplicaciÃ³n
app = FastAPI(
    title="MemoraX Backend",
    description="API para el proyecto MemoraX",
    version="0.1.0"
)

# Ruta de verificaciÃ³n de estado
@app.get("/health")
async def health_check():
    return {"status": "ok"}

# Incluir rutas de usuarios v1
app.include_router(usuarios_v1_router, prefix="/api")