from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from database import Base


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    slug = Column(String(100), nullable=False, unique=True)


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    slug = Column(String(100), nullable=False, unique=True)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    in_stock = Column(Boolean, default=True, nullable=False)
    price_on_request = Column(Boolean, default=True, nullable=False)
