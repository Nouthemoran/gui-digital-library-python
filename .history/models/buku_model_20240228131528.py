from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Buku(Base):
    __tablename__ = 'buku'

    id_buku = Column(Integer, primary_key=True, autoincrement=True)
    judul = Column(String(200), nullable=False)
    penulis = Column(String(100), nullable=False)
    penerbit = Column(String(100), nullable=False)
    tahunterbit = Column(Integer, nullable=False)
    
    # Definisi relasi dengan tabel KategoriBuku (dengan penulisan nama tabel yang benar)
    kategori_id = Column(Integer, ForeignKey('kategoribuku.kategori_id'))
    kategori = relationship("KategoriBuku", backref="buku")



