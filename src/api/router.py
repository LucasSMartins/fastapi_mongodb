from src.api.endpoints.recipes import router
from fastapi import APIRouter


recipes_router = APIRouter()
recipes_router.include_router(router, prefix='/recipes')