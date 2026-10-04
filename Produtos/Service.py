from sqlalchemy.ext.asyncio import AsyncSession
from .Repository import ProductRepository

class ProductService:

    @staticmethod
    async def get_all(session : AsyncSession):
        return await ProductRepository.get_all(session)

    @staticmethod
    async def get_by_id(session : AsyncSession, product_id : int):
        return await ProductRepository.get(session, product_id)

    @staticmethod
    async def get_recommendation_candidates(
        session: AsyncSession,
        **filters: int | None,
    ):
        """Retorna candidatos de recomendação usando uma única consulta."""
        return await ProductRepository.get_recommendation_candidates(session, **filters)

