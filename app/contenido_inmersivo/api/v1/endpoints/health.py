from fastapi import APIRouter

router = APIRouter(prefix="/contenido-inmersivo", tags=["contenido_inmersivo"])

@router.get("/health")
async def health_check_contenido_inmersivo():
    return {"status": "ok", "module": "contenido_inmersivo"}