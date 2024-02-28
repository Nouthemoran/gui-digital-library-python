from tkinter import messagebox
from sqlalchemy.exc import IntegrityError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.user_model import User

# Buat engine untuk koneksi ke database
engine = create_engine('mysql+mysqlconnector://username:password@localhost/digital_library')

# Buat session
Session = sessionmaker(bind=engine)
session = Session()

def register(username, password, email, alamat, namalengkap, role):
    try:
        # Buat objek user baru
        new_user = User(username=username, password=password, email=email, alamat=alamat, namalengkap=namalengkap, role=role)
        # Tambahkan user baru ke dalam session
        session.add(new_user)
        # Commit perubahan ke dalam database
        session.commit()
        messagebox.showinfo("Register", "Pendaftaran berhasil")
    except IntegrityError:
        messagebox.showerror("Register", "Username atau email sudah digunakan")

# Contoh penggunaan
register("new_user", "password", "new_user@example.com", "Alamat New User", "New User", "peminjam")
