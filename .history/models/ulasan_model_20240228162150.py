from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class UlasanBuku(Base):
    __tablename__ = 'ulasan_buku'

    id_ulasan = Column(Integer, primary_key=True, autoincrement=True)
    user = Column(Integer, ForeignKey('users.id_user'), nullable=False)
    buku_id = Column(Integer, ForeignKey('buku.id_buku'), nullable=False)
    ulasan = Column(Text, nullable=False)
    rating = Column(Integer, nullable=False)

    user = relationship("User", backref="ulasan_buku")
    buku = relationship("Buku", backref="ulasan_buku")
