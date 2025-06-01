from fastapi import APIRouter
from .routes.teacher import router as teacher_router

router = APIRouter()

router.include_router(teacher_router, prefix="/teachers", tags=["teachers"])


@router.get("/")
def read_root():
    return {"message": "api rodando"}
