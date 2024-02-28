from sqlalchemy import Column, Integer, Date, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Peminjaman(Base):
    __tablename__ = 'peminjaman'

    peminjaman_id = Column(Integer, primary_key=True, autoincrement=True)
    user = Column(Integer, ForeignKey('users.id_user'), nullable=False)
    buku_id = Column(Integer, ForeignKey('buku.id_buku'), nullable=False)
    tanggalpeminjaman = Column(Date, nullable=False)
    tanggalpengembalian = Column(Date)
    statuspeminjaman = Column(String(20), nullable=False, default="dipinjam")

    user = relationship("User", backref="peminjaman")
    buku = relationship("Buku", backref="peminjaman")
