from sqlalchemy.ext.asyncio import AsyncSession

from .Model import UserProfile
from .Schemas import UserProfileCreate
from .Repository import UserProfileRepository

class UserProfileService:

    @staticmethod
    async def add(session : AsyncSession, userProfile : UserProfileCreate):
        profile = UserProfile(**userProfile.model_dump())

        UserProfileRepository.add(session, profile)
        await session.commit()

    @staticmethod
    async def get(session : AsyncSession, userProfile : UserProfile, userProfile_id : int):
        return await UserProfileRepository.get(session, userProfile, userProfile_id)

    @staticmethod
    async def get_by_user_id(session : AsyncSession, user_id : int):
        return await UserProfileRepository.get_by_user_id(session, user_id)



