from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from Core.db import get_session

from .Service import ProductService

router = APIRouter(prefix= "/produtos")

@router.get("/")
async def get_all(db : AsyncSession = Depends(get_session)):

    return await ProductService.get_all(db)