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
