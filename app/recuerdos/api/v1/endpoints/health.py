from fastapi import APIRouter

router = APIRouter(prefix="/recuerdos", tags=["recuerdos"])

@router.get("/health")
async def health_check_recuerdos():
    return {"status": "ok", "module": "recuerdos"}