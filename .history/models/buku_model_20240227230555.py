from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class KategoriBuku(Base):
    __tablename__ = 'kategori_buku'

    kategori_id = Column(Integer, primary_key=True, autoincrement=True)
    namakategori = Column(String(100), nullable=False, unique=True)
