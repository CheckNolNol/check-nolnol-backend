from fastapi import APIRouter

from app.api.member_router import member_router

api_router = APIRouter()
api_router.include_router(router=member_router, prefix="/member", tags=["Member"])
