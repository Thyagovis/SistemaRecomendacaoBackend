from sqlalchemy import ForeignKey, String, ARRAY
from sqlalchemy.orm import Mapped, mapped_column

from Core.db import Base

class UserProfile(Base):

    __tablename__ = "user_profiles"

    id : Mapped[int] = mapped_column(autoincrement= True, primary_key= True, index= True)
    user_id : Mapped[int] = mapped_column(ForeignKey("users.id"), nullable= False, unique= True)
    main_usage : Mapped[str] = mapped_column(String(50), nullable= False)
    priorities : Mapped[list[str]] = mapped_column(ARRAY(String), nullable= False)
    tech_profile : Mapped[str] = mapped_column(String(50), nullable= False)
    budget : Mapped[str] = mapped_column(String(50), nullable= False)
    pain_point : Mapped[str] = mapped_column(String(50), nullable= False)

