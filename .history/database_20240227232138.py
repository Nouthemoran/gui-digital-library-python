from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.buku_model

# Buat engine untuk koneksi ke database
engine = create_engine('mysql+mysqlconnector://root:@localhost/gui_digital_library')

# Buat sesi
Session = sessionmaker(bind=engine)
session = Session()

# Buat semua tabel yang diperlukan jika belum ada
Base.metadata.create_all(engine)
