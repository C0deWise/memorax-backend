from fastapi import FastAPI
from app.core.config import settings
from app.core.database import engine, Base
from app.usuarios.api.v1.endpoints import login

# Instancia de la aplicaciÃ³n
app = FastAPI(
    title="MemoraX Backend",
    description="API para el proyecto MemoraX",
    version="0.1.0"
)

# Incluir rutas
app.include_router(login.router)

# Ruta de verificaciÃ³n de estado
@app.get("/health")
async def health_check():
    return {"status": "ok"}