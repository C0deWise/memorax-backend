from fastapi import FastAPI
from app.core.config import Settings
from app.core.database import engine, Base

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

# Incluir rutas (aÃ±adir cuando estÃ©n disponibles)
# app.include_router(api_router, prefix="/api/v1")