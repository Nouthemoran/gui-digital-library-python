from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

Base = declarative_base()

class KoleksiPribadi(Base):
    __tablename__ = 'koleksi_pribadi'

    koleksi_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id_user'), nullable=False)
    buku_id = Column(Integer, ForeignKey('buku.id_buku'), nullable=False)

    user = relationship("User", backref="koleksi_pribadi")
    buku = relationship("Buku", backref="koleksi_pribadi")
