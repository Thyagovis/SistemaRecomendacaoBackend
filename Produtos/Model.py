from Core.db import Base

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Numeric


class Product(Base):

    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True, index= True)
    rating: Mapped[float] = mapped_column(Numeric(2, 1), nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    camera: Mapped[str] = mapped_column(String(11), nullable=False)
    display_type: Mapped[str] = mapped_column(String(11), nullable=False)
    display_size: Mapped[float] = mapped_column(Numeric(3, 1), nullable=False)
    battery: Mapped[int] = mapped_column(Integer, nullable=False)
    storage: Mapped[int] = mapped_column(Integer, nullable=False)
    ram: Mapped[int] = mapped_column(Integer, nullable=False)
    weight: Mapped[float] = mapped_column(Numeric(3, 1), nullable=False)
    processor : Mapped[str] = mapped_column(String(28))
    image_url : Mapped[str] = mapped_column(String)

