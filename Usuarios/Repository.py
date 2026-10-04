from sqlalchemy.ext.asyncio import AsyncSession

from .Model import User

class UserRepository:

    @staticmethod
    def add(session : AsyncSession, user : User):
        session.add(user)

    @staticmethod
    async def get(session : AsyncSession, user_id):
        return await session.get(User, user_id)

