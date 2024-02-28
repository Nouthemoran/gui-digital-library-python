from tkinter import messagebox
from sqlalchemy.exc import IntegrityError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.user_model import User

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

