from pydantic_ai import Agent
from pydantic_ai.models.google import GoogleModel
from pydantic_ai.providers.google import GoogleProvider
from sqlalchemy.ext.asyncio import AsyncSession
from .RecomendacaoTools import get_recommendation_candidates
from .ProfileDeps import ProfileDeps

from Core.config import settings


class RecomendationAgent:

    model = GoogleModel(
        "gemini-3.1-flash-lite",
        provider=GoogleProvider(api_key=settings.google_api_key)
    )

    agent = Agent(
        model=model,
        instructions= """
        Você é um agente de recomendação de produtos. Sua função é analisar o perfil do usuário e identificar, entre os produtos disponíveis, quais são mais compatíveis com suas necessidades.
        Considere principalmente: uso principal, prioridades, perfil tecnológico, orçamento e pontos de dor.
        Consulte os produtos disponíveis através da tool uma única vez antes de recomendar. Use todos os filtros que conseguir inferir do perfil e compare os atributos reais dos produtos.
        Retorne somente os IDs dos produtos compatíveis. Nunca invente produtos ou IDs e não recomende produtos que não estejam disponíveis nas tools.""",
    )

    agent.tool(get_recommendation_candidates)


    @staticmethod
    async def get_for_you(prompt : str, session : AsyncSession):

        deps = ProfileDeps(session)

        return await RecomendationAgent.agent.run(prompt, deps= deps)
