from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from Core.db import get_session
from .Schemas import UserCreate
from PerfisUsuarios.Schemas import UserProfileCreate

from .Services import UserServices
from PerfisUsuarios.Service import UserProfileService

router = APIRouter(prefix="/user")

@router.post("/")
async def add(userIn : UserCreate, session : AsyncSession = Depends(get_session)):

    await UserServices.add(session, userIn)

@router.post("/perfil")
async def add_persona(userProfileIn : UserProfileCreate, session : AsyncSession = Depends(get_session)):

    await UserProfileService.add(session, userProfileIn)

@router.get("/recommend")
async def get_for_you(user_id : int, session : AsyncSession = Depends(get_session)):

    return await UserServices.get_for_you(session, user_id)
