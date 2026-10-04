from contextlib import asynccontextmanager

from fastapi import FastAPI

from Core.db import Base, engine

from Produtos.Model import Product
from Usuarios.Model import User
from PerfisUsuarios.Model import UserProfile

from Produtos.Controller import router as produto_router
from Usuarios.Controller import router as usuario_router



@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)

    yield

    await engine.dispose()


app = FastAPI(title="Sistema de Recomendação", lifespan=lifespan)
app.include_router(produto_router)
app.include_router(usuario_router)
