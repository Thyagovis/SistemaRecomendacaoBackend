from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from .Model import UserProfile

class UserProfileRepository:

    @staticmethod
    def add(session : AsyncSession, userProfile : UserProfile):
        session.add(userProfile)

    @staticmethod
    async def get(session : AsyncSession, userProfile : UserProfile, userProfile_id : int):
        return await session.get(userProfile, userProfile_id)

    @staticmethod
    async def get_by_user_id(session : AsyncSession, user_id):

        result = await session.execute(
            select(UserProfile).where(UserProfile.user_id == user_id)
        )

        return result.scalar_one_or_none()