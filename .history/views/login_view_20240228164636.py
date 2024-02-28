from tkinter import messagebox
from models.user_model import User
from database import session

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
