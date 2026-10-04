from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import Integer, and_, cast, func, select
from .Model import Product


class ProductRepository:

    @staticmethod
    def add(session : AsyncSession, product : Product):
        session.add(product)

    @staticmethod
    async def delete(session : AsyncSession, product : Product):
        await session.delete(product)

    @staticmethod
    async def get(session : AsyncSession, product_id : int):
        return await session.get(Product, product_id)

    @staticmethod
    async def get_all(session : AsyncSession, limit : int = 20, ):

        query = (
            select(Product)
            .order_by(func.random())
            .limit(limit)
        )

        result = await session.execute(query)
        return result.scalars().all()

    @staticmethod
    async def get_recommendation_candidates(
        session: AsyncSession,
        *,
        min_price: int | None = None,
        max_price: int | None = None,
        min_camera: int | None = None,
        max_camera: int | None = None,
        min_battery: int | None = None,
        max_battery: int | None = None,
        min_storage: int | None = None,
        max_storage: int | None = None,
        min_ram: int | None = None,
        max_ram: int | None = None,
        limit: int = 25,

    ):
        """Busca os candidatos de recomendação em uma única consulta.

        Todos os filtros são opcionais. Quando mais de um filtro é informado,
        o produto precisa atender a todos eles.
        """
        filters = []

        # A coluna camera contém valores como "50 MP". Extrai-se o valor
        # numérico para que o filtro continue funcionando sem mudar os dados
        # já existentes no banco.
        camera_value = cast(
            func.nullif(func.regexp_replace(Product.camera, r"\D", "", "g"), ""),
            Integer,
        )
        fields = (
            (Product.price, min_price, max_price),
            (camera_value, min_camera, max_camera),
            (Product.battery, min_battery, max_battery),
            (Product.storage, min_storage, max_storage),
            (Product.ram, min_ram, max_ram),
        )

        for field, min_value, max_value in fields:
            if min_value is not None:
                filters.append(field >= min_value)
            if max_value is not None:
                filters.append(field <= max_value)

        query = select(Product)
        if filters:
            query = query.where(and_(*filters))

        result = await session.execute(query.order_by(func.random()).limit(limit))
        return result.scalars().all()
