from Core.db import Base

from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime, func


class User(Base):

    __tablename__ = "users"

    id : Mapped[int] = mapped_column(primary_key=True, index= True, autoincrement= True)
    name : Mapped[str] = mapped_column(String(100), nullable= False)
    email : Mapped[str] = mapped_column(String(150), nullable= False, unique= True)
    password : Mapped[str] = mapped_column(String(20), nullable= False)
    created_at : Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default= func.now(), nullable= False)
    updated_at : Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default= func.now(), nullable= False)

