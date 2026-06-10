from fastapi import APIRouter

router = APIRouter(prefix="/contenido-multimedia", tags=["contenido_multimedia"])

@router.get("/health")
async def health_check_contenido_multimedia():
    return {"status": "ok", "module": "contenido_multimedia"}