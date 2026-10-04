from pydantic_ai import RunContext
from Produtos.Service import ProductService

from .ProfileDeps import ProfileDeps


def product_to_dict(product):
    """Converte o modelo do SQLAlchemy em dados serializáveis pela tool."""
    return dict(
        id=product.id,
        rating=float(product.rating),
        price=product.price,
        camera=product.camera,
        display_type=product.display_type,
        display_size=float(product.display_size),
        battery=product.battery,
        storage=product.storage,
        ram=product.ram,
        weight=float(product.weight),
        processor=product.processor,
    )


async def get_recommendation_candidates(
    ctx: RunContext[ProfileDeps],
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
):
    """Busca, em uma única consulta, produtos compatíveis com o perfil.

    Informe apenas os limites que puder inferir do perfil. Os limites de
    preço, câmera (MP), bateria (mAh), armazenamento (GB) e RAM (GB) são
    combinados na mesma busca; portanto, chame esta tool somente uma vez.
    """
    products = await ProductService.get_recommendation_candidates(
        ctx.deps.session,
        min_price=min_price,
        max_price=max_price,
        min_camera=min_camera,
        max_camera=max_camera,
        min_battery=min_battery,
        max_battery=max_battery,
        min_storage=min_storage,
        max_storage=max_storage,
        min_ram=min_ram,
        max_ram=max_ram,
    )
    return [product_to_dict(product) for product in products]
