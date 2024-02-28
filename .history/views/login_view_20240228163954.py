from tkinter import messagebox
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.user_model import User

# Buat engine untuk koneksi ke database
engine = create_engine('mysql+mysqlconnector://username:password@localhost/digital_library')

# Buat session
Session = sessionmaker(bind=engine)
session = Session()

def login(username, password):
    # Cari pengguna berdasarkan username dan password
    user = session.query(User).filter_by(username=username, password=password).first()

    if user:
        if user.role == "admin":
            messagebox.showinfo("Login", "Login berhasil sebagai admin")
            # Lakukan navigasi ke halaman dashboard admin
        elif user.role == "petugas":
            messagebox.showinfo("Login", "Login berhasil sebagai petugas")
            # Lakukan navigasi ke halaman dashboard petugas
        elif user.role == "peminjam":
            messagebox.showinfo("Login", "Login berhasil sebagai peminjam")
            # Lakukan navigasi ke halaman dashboard peminjam
    else:
        messagebox.showerror("Login", "Username atau password salah")

# Contoh penggunaan
login("admin", "admin")  # Ganti dengan nilai input dari antarmuka pengguna
