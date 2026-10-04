from sqlalchemy.ext.asyncio import AsyncSession

from .Repository import UserRepository
from .Schemas import UserCreate
from .Model import User
from Produtos.Service import ProductService

from PerfisUsuarios.Service import UserProfileService
from Recomendacao.AgenteRecomendacao import RecomendationAgent

class UserServices:

    @staticmethod
    async def get(session : AsyncSession, user_id : int):
        return await UserRepository.get(session, user_id)

    @staticmethod
    async def add(session : AsyncSession, userIn : UserCreate):
        user = User(**userIn.model_dump())

        session.add(user)
        await session.commit()

    @staticmethod
    async def get_for_you(session : AsyncSession, user_id : int):

        profile = await UserProfileService.get_by_user_id(session, user_id)
        profile_data = dict(
            id=profile.id,
            user_id=profile.user_id,
            main_usage=profile.main_usage,
            priorities=profile.priorities,
            tech_profile=profile.tech_profile,
            budget=profile.budget,
            pain_point=profile.pain_point,
        )

        prompt = f"""
        Analise o perfil do usuário abaixo e recomende os produtos mais
        compatíveis com suas necessidades.
        
        Considere uso principal, prioridades, perfil tecnológico,
        orçamento e pontos de dor.
        
        Consulte os produtos disponíveis usando as tools.
        
        Retorne apenas os IDs dos produtos recomendados.
        
        Perfil:
        {profile_data}
        """

        ids_results = (await RecomendationAgent.get_for_you(session= session, prompt= prompt)).output
        ids = []
        for i in ids_results.split(","):
            ids.append(int(i))

        results = []
        for id in ids:
            results.append(await ProductService.get_by_id(session, id))


        return results
