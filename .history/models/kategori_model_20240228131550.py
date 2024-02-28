from sqlalchemy import Column, Integer, String
from database import Base 

Base = declarative_base()

class KategoriBuku(Base):
    __tablename__ = 'kategoribuku'

    kategori_id = Column(Integer, primary_key=True, autoincrement=True)
    namakategori = Column(String(100), nullable=False, unique=True)
