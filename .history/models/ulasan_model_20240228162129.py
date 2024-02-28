from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class UlasanBuku(Base):
    __tablename__ = 'ulasan_buku'

    ulasan_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id_user'), nullable=False)
    buku_id = Column(Integer, ForeignKey('buku.id_buku'), nullable=False)
    ulasan = Column(Text, nullable=False)
    rating = Column(Integer, nullable=False)

    user = relationship("User", backref="ulasan_buku")
    buku = relationship("Buku", backref="ulasan_buku")
