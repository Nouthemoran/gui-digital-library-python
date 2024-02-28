from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.buku_model import Base

# Buat engine untuk koneksi ke database
engine = create_engine('mysql+mysqlconnector://root:@localhost/gui_digital_library')

# Buat sesi
Session = sessionmaker(bind=engine)
session = Session()

# Buat semua tabel yang diperlukan jika belum ada
Base.metadata.create_all(engine)

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Buat objek Base untuk mendefinisikan model
Base = declarative_base()

# Buat engine untuk koneksi ke database (sesuaikan dengan jenis database yang Anda gunakan)
engine = create_engine('mysql+mysqlconnector://root:@localhost/gui_digital_library')

# Buat sesi untuk berinteraksi dengan database
Session = sessionmaker(bind=engine)
session = Session()
